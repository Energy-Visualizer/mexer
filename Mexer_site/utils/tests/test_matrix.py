from unittest.mock import MagicMock, patch

import altair as alt
from django.test import TransactionTestCase
from Mexer.models import PSUT
from scipy.sparse import coo_matrix

from utils.matrix import get_matrix, get_ruvy_matrix, visualize_matrix


class MatrixTests(TransactionTestCase):
    def test_get_matrix_empty(self):
        with patch("utils.matrix.query_database", return_value=[]):
            mat = get_matrix(("default", PSUT), {"Year": 2020})
            self.assertEqual(mat.nnz, 0)

    def test_get_matrix_with_values(self):
        sparse = [(0, 1, 2.5), (1, 0, 3.0)]
        with patch("utils.matrix.query_database", return_value=sparse):
            mat = get_matrix(("default", PSUT), {"Year": 2020})
            self.assertEqual(mat.shape, (2, 2))
            arr = mat.toarray()
            self.assertEqual(arr[0, 1], 2.5)
            self.assertEqual(arr[1, 0], 3.0)

    def test_get_ruvy_matrix_empty(self):
        with patch("utils.matrix.query_database", return_value=[]):
            mat, names = get_ruvy_matrix(("default", PSUT), {"Year": 2020})
            self.assertIsNone(mat)
            self.assertIsNone(names)

    def test_get_ruvy_matrix_with_values(self):
        sparse = [(0, 1, 2.5, "A"), (1, 0, 3.0, "B")]
        with patch("utils.matrix.query_database", return_value=sparse):
            with patch("utils.matrix.Index") as MockIndex:
                MockIndex.objects = MagicMock()
                MockIndex.objects.all.return_value.count.return_value = 3

                mat, names = get_ruvy_matrix(("default", PSUT), {"Year": 2020})
                assert mat is not None

                # names should be the tuple of matname values
                self.assertEqual(names, ("A", "B"))
                self.assertEqual(mat.shape, (3, 3))
                arr = mat.toarray()
                self.assertEqual(arr[0, 1], 2.5)

    def test_visualize_matrix_basic_and_ruvy(self):
        mat = coo_matrix(([2.5, 3.0], ([0, 1], [1, 0])), shape=(3, 3))

        with patch("utils.matrix.Index") as MockIndex:
            MockIndex.objects = MagicMock()
            MockIndex.objects.values_list.return_value = [(0, 0), (1, 1), (2, 2)]

            # Patch Translator to provide index and matname translations
            translator_instance = MagicMock()
            translator_instance.index_translate.side_effect = lambda x: f"IDX{x}"
            translator_instance.matname_translate.side_effect = lambda x: f"MAT{x}"

            with patch("utils.matrix.Translator", return_value=translator_instance):
                heatmap = visualize_matrix(
                    ("default", PSUT), mat, color_scale="viridis"
                )
                self.assertIsInstance(heatmap, alt.Chart)

                heatmap_ruvy = visualize_matrix(
                    ("default", PSUT), mat, matnames=("A", "B"), coloring_method="ruvy"
                )
                self.assertIsInstance(heatmap_ruvy, alt.Chart)
