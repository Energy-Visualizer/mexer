from django.test import TransactionTestCase
from Mexer.models import PSUT, AggEtaPFU

from utils.data import get_dataframe

VERSION_QUERY_YEARS = [1800, 1801, 1802]


class PSUTVersionTests(TransactionTestCase):
    def _query(self, version: int):
        return get_dataframe(
            target=("default", PSUT),
            query={
                "ValidFromVersion__lte": version,
                "ValidToVersion__gte": version,
                "Year__in": VERSION_QUERY_YEARS,  # isolate our test rows
            },
            columns=["Year", "ValidFromVersion", "ValidToVersion"],
        )

    def test_version_1_returns_correct_rows(self):
        df = self._query(1)
        years = set(df["Year"])
        self.assertIn(1800, years)  # valid only at v1
        self.assertIn(1801, years)  # valid v1-v2
        self.assertNotIn(1802, years)  # only valid from v2+

    def test_version_2_returns_correct_rows(self):
        df = self._query(2)
        years = set(df["Year"])
        self.assertNotIn(1800, years)  # expired after v1
        self.assertIn(1801, years)  # valid v1-v2
        self.assertIn(1802, years)  # valid v2 to INT32_MAX

    def test_version_3_returns_only_open_ended_row(self):
        df = self._query(3)
        years = set(df["Year"])
        self.assertNotIn(1800, years)
        self.assertNotIn(1801, years)
        self.assertIn(1802, years)  # INT32_MAX row still open

    def test_version_0_returns_no_rows(self):
        df = self._query(0)
        self.assertTrue(df.empty)


class AggEtaPFUVersionTests(TransactionTestCase):
    def _query(self, version: int):
        return get_dataframe(
            target=("default", AggEtaPFU),
            query={
                "ValidFromVersion__lte": version,
                "ValidToVersion__gte": version,
                "Year__in": VERSION_QUERY_YEARS,
            },
            columns=["Year", "ValidFromVersion", "ValidToVersion"],
        )

    def test_version_1_returns_correct_rows(self):
        df = self._query(1)
        years = set(df["Year"])
        self.assertIn(1800, years)
        self.assertIn(1801, years)
        self.assertNotIn(1802, years)

    def test_version_2_returns_correct_rows(self):
        df = self._query(2)
        years = set(df["Year"])
        self.assertNotIn(1800, years)
        self.assertIn(1801, years)
        self.assertIn(1802, years)

    def test_version_3_returns_only_open_ended_row(self):
        df = self._query(3)
        years = set(df["Year"])
        self.assertNotIn(1800, years)
        self.assertNotIn(1801, years)
        self.assertIn(1802, years)

    def test_version_0_returns_no_rows(self):
        df = self._query(0)
        self.assertTrue(df.empty)
