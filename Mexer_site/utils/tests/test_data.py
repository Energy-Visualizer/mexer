from django.conf import settings
from django.http import QueryDict
from django.test import TransactionTestCase
from Mexer.models import AggEtaPFU, IEAData, PSUTReAllChopAllDsAllGrAll
from Mexer.models import PSUTReAllChopAllDsAllGrAll as PSUT

from utils.data import (
    get_csv_from_query,
    get_database_target,
    get_dataframe,
    get_excel_from_query,
    get_userfriendly_dataframe,
    query_database,
    shape_post_request,
    translate_query,
)


class DataTests(TransactionTestCase):
    def test_get_database_target(self):
        query = {"dataset": "CL-PFU IEA", "plot_type": "xy_plot"}
        target = get_database_target(query)
        self.assertEqual(target, ("default", AggEtaPFU))

        query = {"dataset": f"{settings.SANDBOX_PREFIX}CL-PFU IEA"}
        target = get_database_target(query)
        self.assertEqual(target, ("sandbox", PSUTReAllChopAllDsAllGrAll))

    def test_query_database_valid(self):
        target = ("default", PSUT)
        query = {"year": 2020}
        values = ["year", "value"]
        data = query_database(target, query, values)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][0], 2020)
        self.assertEqual(data[0][1], 10.0)

    def test_query_database_invalid(self):
        target = ("invalid_db", PSUT)
        query = {"year": 2021}
        values = ["year", "value"]
        with self.assertRaises(ValueError):
            query_database(target, query, values)

    def test_get_dataframe(self):
        target = ("default", PSUT)
        query = {"year": 2021}
        columns = ["year", "value"]
        df = get_dataframe(target, query, columns)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["year"], 2021)
        self.assertEqual(df.iloc[0]["value"], 5.5)

    def test_get_translated_dataframe(self):
        target = ("default", PSUT)
        query = {"year": 2021}
        columns = ["year", "value"]
        df = get_userfriendly_dataframe(target, query, columns)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["year"], 2021)
        self.assertEqual(df.iloc[0]["value"], 5.5)

    def test_get_csv_from_query(self):
        target = ("default", PSUT)
        query = {"year": 2021}
        columns = ["year", "value"]
        csv_data = get_csv_from_query(target, query, columns)
        self.assertIn("year,value", csv_data)
        self.assertIn("2021,5.5", csv_data)

    def test_get_excel_from_query(self):
        target = ("default", PSUT)
        query = {"year": 2021}
        columns = ["year", "value"]
        excel_data = get_excel_from_query(target, query, columns)
        self.assertTrue(isinstance(excel_data, bytes))

    def test_shape_post_request(self):
        q = QueryDict("", mutable=True)
        q["csrfmiddlewaretoken"] = "dummy_token"
        q["dataset"] = "CL-PFU IEA"
        q["plot_type"] = "xy_plot"
        shaped_query, plot_type, db_target = shape_post_request(q)
        self.assertNotIn("csrfmiddlewaretoken", shaped_query)
        self.assertEqual(plot_type, "xy_plot")
        self.assertEqual(db_target, ("default", AggEtaPFU))

    def test_translate_query(self):
        target = ("default", PSUT)
        query = {"dataset": "CL-PFU IEA", "year": "2021"}
        translated_query = translate_query(target, query)
        self.assertIn("dataset", translated_query)
        self.assertIn("year", translated_query)
        self.assertEqual(translated_query["year"], 2021)
