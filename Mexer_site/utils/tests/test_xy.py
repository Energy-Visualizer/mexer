from django.test import TestCase
from Mexer.models import AggEtaPFU

from utils.xy_plot import get_xy


class XYTests(TestCase):
    def test_get_xy(self):
        # Define test parameters
        efficiency_metric = "etapf"
        target = ("default", AggEtaPFU)
        query = {"country": 1}
        color_by = "country"
        line_by = "energy_type"
        facet_col_by = None
        facet_row_by = None
        energy_type = "Energy"

        # Call the function to test
        fig = get_xy(
            efficiency_metric,
            target,
            query,
            color_by,
            line_by,
            facet_col_by,
            facet_row_by,
            energy_type,
        )

        # Check if the returned figure is not None
        self.assertIsNotNone(fig)
