import json
from django.test import TransactionTestCase
from utils.sankey import (
    get_sankey,
    _get_sankey_color,
    _create_new_node,
    _get_node_info,
    NodeInfo,
)
from Mexer.models import PSUT
from collections import Counter


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
        """_create_new_node should create and register a new node."""
        node_info_by_name = {}
        indexes_by_col = Counter()
        sankey_orders = {"test_node": 0}
        
        node_info = _create_new_node("test_node", node_info_by_name, indexes_by_col, sankey_orders)
        
        # Node should be created with correct column
        self.assertEqual(node_info.column, 0)
        self.assertEqual(node_info.index, 0)
        
        # Node should be registered
        self.assertIn("test_node", node_info_by_name)
        self.assertEqual(node_info_by_name["test_node"], node_info)
        
        # Index counter should be incremented
        self.assertEqual(indexes_by_col[0], 1)

    def test_create_new_node_multiple_in_column(self):
        """_create_new_node should assign incrementing indices in same column."""
        node_info_by_name = {}
        indexes_by_col = Counter()
        sankey_orders = {"node1": 0, "node2": 0}
        
        node1 = _create_new_node("node1", node_info_by_name, indexes_by_col, sankey_orders)
        node2 = _create_new_node("node2", node_info_by_name, indexes_by_col, sankey_orders)
        
        self.assertEqual(node1.column, 0)
        self.assertEqual(node1.index, 0)
        self.assertEqual(node2.column, 0)
        self.assertEqual(node2.index, 1)

    def test_get_node_info_existing(self):
        """_get_node_info should return existing node."""
        node_info_by_name = {"existing_node": NodeInfo(0, 1)}
        
        result = _get_node_info("existing_node", node_info_by_name)
        
        self.assertEqual(result.column, 0)
        self.assertEqual(result.index, 1)

    def test_get_node_info_missing(self):
        """_get_node_info should raise KeyError for missing node."""
        node_info_by_name = {}
        
        with self.assertRaises(KeyError):
            _get_node_info("nonexistent_node", node_info_by_name)

    def test_get_sankey_no_data(self):
        """get_sankey should return None tuple if no data found."""
        target = ("default", PSUT)
        query = {"Year": 9999}  # Year that doesn't exist in test data
        
        result = get_sankey(target, query)
        
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], None)
        self.assertEqual(result[2], None)

    def test_get_sankey_returns_json_strings(self):
        """get_sankey should return JSON strings for nodes, links, and options."""
        target = ("default", PSUT)
        query = {"Year": 2020}
        
        result = get_sankey(target, query)
        
        # Should return nodes, links, options, max_columns
        self.assertEqual(len(result), 4)
        
        nodes_json, links_json, options_json, max_columns = result
        
        nodes = json.loads(nodes_json)
        self.assertIsInstance(nodes, list)
        
        links = json.loads(links_json)
        self.assertIsInstance(links, list)
        
        options = json.loads(options_json)
        self.assertIsInstance(options, dict)
        
        # max_columns should be an integer
        self.assertIsInstance(max_columns, int)
        self.assertGreater(max_columns, 0)

    def test_get_sankey_nodes_structure(self):
        """get_sankey nodes should have correct structure."""
        target = ("default", PSUT)
        query = {"Year": 2020}
        
        nodes_json, links_json, options_json, max_columns = get_sankey(target, query)
        
        nodes = json.loads(nodes_json)
        
        # Nodes should be a list of columns
        self.assertIsInstance(nodes, list)
        
        # Each column should be a list of node dicts
        for column in nodes:
            self.assertIsInstance(column, list)
            for node in column:
                self.assertIn("label", node)
                self.assertIn("color", node)
                self.assertIsInstance(node["label"], str)
                self.assertIsInstance(node["color"], str)

    def test_get_sankey_links_structure(self):
        """get_sankey links should have correct structure."""
        target = ("default", PSUT)
        query = {"Year": 2020}
        
        nodes_json, links_json, options_json, max_columns = get_sankey(target, query)
        
        links = json.loads(links_json)
        
        # Links should be a list
        self.assertIsInstance(links, list)
        
        # Each link should have from, to, value, color
        for link in links:
            self.assertIn("from", link)
            self.assertIn("to", link)
            self.assertIn("value", link)
            self.assertIn("color", link)
            
            # from and to should have column and node
            self.assertIn("column", link["from"])
            self.assertIn("node", link["from"])
            self.assertIn("column", link["to"])
            self.assertIn("node", link["to"])
            
            # value should be numeric
            self.assertIsInstance(link["value"], (int, float))

    def test_get_sankey_options_structure(self):
        """get_sankey options should have expected keys."""
        target = ("default", PSUT)
        query = {"Year": 2020}
        
        nodes_json, links_json, options_json, max_columns = get_sankey(target, query)
        
        options = json.loads(options_json)
        
        # Check for expected option keys
        self.assertIn("plot_background_color", options)
        self.assertIn("default_links_opacity", options)
        self.assertIn("default_gradient_links_opacity", options)
        self.assertIn("show_column_lines", options)
        self.assertIn("show_column_names", options)
        self.assertIn("linear_gradient_links", options)
