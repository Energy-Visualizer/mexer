import json
import pickle
from unittest.mock import patch

from django.http import HttpRequest
from django.test import TransactionTestCase

from utils.history import (
    MAX_HISTORY,
    get_history_html,
    get_user_history,
    update_user_history,
)


class HistoryTests(TransactionTestCase):
    def test_get_user_history_no_cookie(self):
        req = HttpRequest()
        self.assertEqual(get_user_history(req), [])

    def test_get_user_history_with_cookie(self):
        req = HttpRequest()
        sample = [{"plot_type": "xy_plot", "dataset": "IEA", "country": "USA"}]
        req.COOKIES["user_history"] = pickle.dumps(sample).hex()
        result = get_user_history(req)
        self.assertEqual(result, sample)

    def test_update_user_history_empty(self):
        req = HttpRequest()
        serialized = update_user_history(
            req, "xy_plot", {"dataset": "D", "country": "C"}
        )
        history = pickle.loads(serialized)
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["plot_type"], "xy_plot")
        self.assertEqual(history[0]["dataset"], "D")
        self.assertEqual(history[0]["country"], "C")

    def test_update_user_history_moves_duplicate_to_front(self):
        initial = [
            {"plot_type": "xy_plot", "dataset": "A", "country": "X"},
            {"plot_type": "bar", "dataset": "B", "country": "Y"},
            {"plot_type": "line", "dataset": "C", "country": "Z"},
        ]
        req = HttpRequest()
        req.COOKIES["user_history"] = pickle.dumps(initial).hex()

        # Duplicate the middle item (bar) by sending same plot_type + fields
        duplicate = initial[1]
        serialized = update_user_history(
            req,
            duplicate["plot_type"],
            {"dataset": duplicate["dataset"], "country": duplicate["country"]},
        )
        updated = pickle.loads(serialized)

        # The duplicated item should now be first and present only once
        self.assertEqual(updated[0]["plot_type"], duplicate["plot_type"])
        self.assertEqual(updated[0]["dataset"], duplicate["dataset"])
        # Ensure no duplicates
        occurrences = sum(1 for item in updated if item == duplicate)
        self.assertEqual(occurrences, 1)

    def test_update_user_history_trims_when_exceeding_max(self):
        initial = [
            {"plot_type": f"p{i}", "dataset": f"D{i}", "country": "C"}
            for i in range(MAX_HISTORY)
        ]
        req = HttpRequest()
        req.COOKIES["user_history"] = pickle.dumps(initial).hex()

        # Add a new unique item
        new_item_query = {"dataset": "NEW", "country": "NEWC"}
        serialized = update_user_history(req, "newplot", new_item_query)
        updated = pickle.loads(serialized)

        # Length should remain MAX_HISTORY and new item should be at the front
        self.assertEqual(len(updated), MAX_HISTORY)
        self.assertEqual(updated[0]["plot_type"], "newplot")
        self.assertEqual(updated[0]["dataset"], "NEW")

    def test_get_history_html_empty(self):
        html = get_history_html([])
        self.assertEqual(html, "<p>No history available.</p>")

    def test_get_history_html_with_items(self):
        history = [
            {"plot_type": "xy_plot", "dataset": "IEA", "country": "US"},
            {"plot_type": "bar", "dataset": "Other", "country": "FR"},
        ]
        # Patch reverse so the generated hx-post has a predictable URL
        with patch("utils.history.reverse", return_value="/delete-history"):
            html = get_history_html(history)

        # Check that each history item's dataset and country appear in the HTML
        self.assertIn("Dataset: IEA", html)
        self.assertIn("Country: US", html)
        self.assertIn("Dataset: Other", html)
        self.assertIn("Country: FR", html)

        # Check that the hx-vals JSON is present for the first item
        self.assertIn(json.dumps(history[0]), html)
        # Ensure the delete endpoint we patched appears
        self.assertIn("/delete-history", html)
