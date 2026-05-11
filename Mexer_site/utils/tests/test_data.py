from django.conf import settings
from django.test import TransactionTestCase
from Mexer.models import PSUT, AggEtaPFU, IEAData

from utils.data import (
    get_csv_from_query,
    get_database_target,
    get_dataframe,
    get_excel_from_query,
    get_translated_dataframe,
    query_database,
    shape_post_request,
    translate_query,
)


class DataTests(TransactionTestCase):
    def test_get_database_target(self):
        query = {"dataset": "IEAEWEB2022", "plot_type": "xy_plot"}
        target = get_database_target(query)
        self.assertEqual(target, ("default", AggEtaPFU))

        query = {"dataset": f"{settings.SANDBOX_PREFIX}IEAEWEB2022"}
        target = get_database_target(query)
        self.assertEqual(target, ("sandbox", IEAData))

    def test_query_database_valid(self):
        target = ("default", PSUT)
        query = {"Year": 2020}
        values = ["Year", "value"]
        data = query_database(target, query, values)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][0], 2020)
        self.assertEqual(data[0][1], 10.0)

    def test_query_database_invalid(self):
        target = ("invalid_db", PSUT)
        query = {"Year": 2021}
        values = ["Year", "value"]
        with self.assertRaises(ValueError):
            query_database(target, query, values)

    def test_get_dataframe(self):
        target = ("default", PSUT)
        query = {"Year": 2021}
        columns = ["Year", "value"]
        df = get_dataframe(target, query, columns)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Year"], 2021)
        self.assertEqual(df.iloc[0]["value"], 5.5)

    def test_get_translated_dataframe(self):
        target = ("default", PSUT)
        query = {"Year": 2021}
        columns = ["Year", "value"]
        df = get_translated_dataframe(target, query, columns)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Year"], 2021)
        self.assertEqual(df.iloc[0]["value"], 5.5)

    def test_get_csv_from_query(self):
        target = ("default", PSUT)
        query = {"Year": 2021}
        columns = ["Year", "value"]
        csv_data = get_csv_from_query(target, query, columns)
        self.assertIn("Year,value", csv_data)
        self.assertIn("2021,5.5", csv_data)

    def test_get_excel_from_query(self):
        target = ("default", PSUT)
        query = {"Year": 2021}
        columns = ["Year", "value"]
        excel_data = get_excel_from_query(target, query, columns)
        self.assertTrue(isinstance(excel_data, bytes))

    def test_shape_post_request(self):
        payload = {
            "csrfmiddlewaretoken": "dummy_token",
            "dataset": "IEAEWEB2022",
            "plot_type": "xy_plot",
        }
        shaped_query, plot_type, db_target = shape_post_request(payload)
        self.assertNotIn("csrfmiddlewaretoken", shaped_query)
        self.assertEqual(plot_type, "xy_plot")
        self.assertEqual(db_target, ("default", AggEtaPFU))

    def test_translate_query(self):
        target = ("default", PSUT)
        query = {"dataset": "Test Dataset", "year": "2021"}
        translated_query = translate_query(target, query)
        self.assertIn("Dataset", translated_query)
        self.assertIn("Year", translated_query)
        self.assertEqual(translated_query["Year"], 2021)
