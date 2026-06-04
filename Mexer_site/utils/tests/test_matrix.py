from unittest.mock import MagicMock, patch

import altair as alt
from django.test import TransactionTestCase
from Mexer.models import PSUTReAllChopAllDsAllGrAll as PSUT
from scipy.sparse import coo_matrix

from utils.matrix import get_matrix, get_ruvy_matrix, visualize_matrix


class MatrixTests(TransactionTestCase):
    def test_get_matrix_empty(self):
        mat = get_matrix(("default", PSUT), {"year": 1000})
        self.assertEqual(mat.nnz, 0)

    def test_get_matrix_with_values(self):
        mat = get_matrix(("default", PSUT), {"year__in": [2020, 2021]})
        self.assertEqual(mat.shape, (4, 4))
        arr = mat.toarray()
        print(arr)
        self.assertEqual(arr[1, 0], 10.0)
        self.assertEqual(arr[0, 1], 5.5)

    def test_get_ruvy_matrix_empty(self):
        result = get_ruvy_matrix(("default", PSUT), {"year": 1000})
        self.assertIsNone(result)

    def test_get_ruvy_matrix_with_values(self):
        result = get_ruvy_matrix(("default", PSUT), {"year__in": [2020, 2021]})
        assert result is not None
        mat, names = result

        # names should be the tuple of matname values
        self.assertEqual(names, (1, 1))
        self.assertEqual(mat.shape, (4, 4))
        arr = mat.toarray()
        print(arr)
        self.assertEqual(arr[1, 0], 10.0)
        self.assertEqual(arr[0, 1], 5.5)

    def test_visualize_matrix_basic_and_ruvy(self):
        mat = coo_matrix(([2.5, 3.0], ([0, 1], [1, 0])), shape=(3, 3))

        heatmap = visualize_matrix(("default", PSUT), mat, color_scale="viridis")
        self.assertIsInstance(heatmap, alt.Chart)

        heatmap_ruvy = visualize_matrix(
            ("default", PSUT), mat, matnames=(1, 2), coloring_method="ruvy"
        )
        self.assertIsInstance(heatmap_ruvy, alt.Chart)
