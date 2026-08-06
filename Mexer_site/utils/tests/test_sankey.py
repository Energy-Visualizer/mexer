import json
from collections import Counter

from django.test import TransactionTestCase
from Mexer.models import PSUTReAllChopAllDsAllGrAll as PSUT

from utils.sankey import (
    NodeInfo,
    _create_new_node,
    _get_node_info,
    _get_sankey_color,
    get_sankey,
)


class SankeyTests(TransactionTestCase):
    def test_get_sankey_color_finds_carrier(self):
        """_get_sankey_color should return color for known carrier."""
        color = _get_sankey_color("electricity")
        self.assertIsInstance(color, str)
        self.assertTrue(len(color) > 0)

    def test_get_sankey_color_unknown_carrier(self):
        """_get_sankey_color should return empty string for unknown carrier."""
        color = _get_sankey_color("unknown_carrier_xyz_abc")
        self.assertEqual(color, "")

    def test_create_new_node(self):
        """_create_new_node should create and register a new node with a flat index."""
        node_info_by_name = {}
        indexes_by_col = Counter()
        sankey_orders = {"test_node": 0}

        node_info = _create_new_node(
            "test_node", node_info_by_name, indexes_by_col, sankey_orders, 0
        )

        # Node should be created with correct column, in-column index, and flat index
        self.assertEqual(node_info.column, 0)
        self.assertEqual(node_info.index, 0)
        self.assertEqual(node_info.flat_index, 0)

        # Node should be registered
        self.assertIn("test_node", node_info_by_name)
        self.assertEqual(node_info_by_name["test_node"], node_info)

        # Index counter should be incremented
        self.assertEqual(indexes_by_col[0], 1)

    def test_create_new_node_multiple_in_column(self):
        """_create_new_node should assign incrementing in-column indices and
        distinct flat indices for nodes added to the same column."""
        node_info_by_name = {}
        indexes_by_col = Counter()
        sankey_orders = {"node1": 0, "node2": 0}

        node1 = _create_new_node(
            "node1", node_info_by_name, indexes_by_col, sankey_orders, 0
        )
        node2 = _create_new_node(
            "node2", node_info_by_name, indexes_by_col, sankey_orders, 1
        )

        self.assertEqual(node1.column, 0)
        self.assertEqual(node1.index, 0)
        self.assertEqual(node1.flat_index, 0)

        self.assertEqual(node2.column, 0)
        self.assertEqual(node2.index, 1)
        self.assertEqual(node2.flat_index, 1)

    def test_get_node_info_existing(self):
        """_get_node_info should return existing node."""
        node_info_by_name = {"existing_node": NodeInfo(0, 1, 5)}

        result = _get_node_info("existing_node", node_info_by_name)

        self.assertEqual(result.column, 0)
        self.assertEqual(result.index, 1)
        self.assertEqual(result.flat_index, 5)

    def test_get_node_info_missing(self):
        """_get_node_info should raise KeyError for missing node."""
        node_info_by_name = {}

        with self.assertRaises(KeyError):
            _get_node_info("nonexistent_node", node_info_by_name)

    def test_get_sankey_no_data(self):
        """get_sankey should return None if no data found."""
        target = ("default", PSUT)
        query = {"year": 9999}  # Year that doesn't exist in test data

        result = get_sankey(target, query)
        self.assertIsNone(result)

    def test_get_sankey_returns_json_strings(self):
        """get_sankey should return JSON strings for nodes, links, and options,
        plus an integer max_columns."""
        target = ("default", PSUT)
        query = {"year": 2020}

        result = get_sankey(target, query)

        # Should return nodes, links, options, max_columns
        assert result is not None
        self.assertEqual(len(result), 4)

        nodes_json, links_json, options_json, max_columns = result

        nodes = json.loads(nodes_json)
        self.assertIsInstance(nodes, dict)

        links = json.loads(links_json)
        self.assertIsInstance(links, dict)

        options = json.loads(options_json)
        self.assertIsInstance(options, dict)

        # max_columns should be an integer
        self.assertIsInstance(max_columns, int)
        self.assertGreater(max_columns, 0)

    def test_get_sankey_nodes_structure(self):
        """get_sankey nodes should be a flat dict of parallel label/color/x lists."""
        target = ("default", PSUT)
        query = {"year": 2020}

        sankey = get_sankey(target, query)
        assert sankey is not None
        nodes_json, *_ = sankey

        nodes = json.loads(nodes_json)

        # Nodes should be a dict with parallel lists
        self.assertIsInstance(nodes, dict)
        self.assertIn("label", nodes)
        self.assertIn("color", nodes)
        self.assertIn("x", nodes)

        self.assertIsInstance(nodes["label"], list)
        self.assertIsInstance(nodes["color"], list)
        self.assertIsInstance(nodes["x"], list)

        # All three lists should be the same length (parallel arrays)
        num_nodes = len(nodes["label"])
        self.assertEqual(len(nodes["color"]), num_nodes)
        self.assertEqual(len(nodes["x"]), num_nodes)
        self.assertGreater(num_nodes, 0)

        for label in nodes["label"]:
            self.assertIsInstance(label, str)
        for color in nodes["color"]:
            self.assertIsInstance(color, str)
        for x in nodes["x"]:
            self.assertIsInstance(x, (int, float))
            self.assertGreaterEqual(x, 0)
            self.assertLessEqual(x, 1)

    def test_get_sankey_links_structure(self):
        """get_sankey links should be a flat dict referencing nodes by index."""
        target = ("default", PSUT)
        query = {"year": 2020}

        sankey = get_sankey(target, query)
        assert sankey is not None
        nodes_json, links_json, *_ = sankey

        nodes = json.loads(nodes_json)
        links = json.loads(links_json)
        num_nodes = len(nodes["label"])

        # Links should be a dict with parallel lists
        self.assertIsInstance(links, dict)
        for key in ("source", "target", "value", "color", "from_label", "to_label"):
            self.assertIn(key, links)

        num_links = len(links["source"])
        for key in ("target", "value", "color", "from_label", "to_label"):
            self.assertEqual(len(links[key]), num_links)
        self.assertGreater(num_links, 0)

        for source, target_idx, value, color, from_label, to_label in zip(
            links["source"],
            links["target"],
            links["value"],
            links["color"],
            links["from_label"],
            links["to_label"],
        ):
            # source/target are flat indices into the node lists
            self.assertIsInstance(source, int)
            self.assertIsInstance(target_idx, int)
            self.assertGreaterEqual(source, 0)
            self.assertLess(source, num_nodes)
            self.assertGreaterEqual(target_idx, 0)
            self.assertLess(target_idx, num_nodes)

            # value should be numeric
            self.assertIsInstance(value, (int, float))

            self.assertIsInstance(color, str)
            self.assertIsInstance(from_label, str)
            self.assertIsInstance(to_label, str)

    def test_get_sankey_options_structure(self):
        """get_sankey options should have expected keys for the Plotly renderer."""
        target = ("default", PSUT)
        query = {"year": 2020}

        sankey = get_sankey(target, query)
        assert sankey is not None
        _, _, options_json, _ = sankey

        options = json.loads(options_json)

        self.assertIn("plot_background_color", options)
        self.assertIn("arrangement", options)
        self.assertIsInstance(options["plot_background_color"], str)
        self.assertIsInstance(options["arrangement"], str)
