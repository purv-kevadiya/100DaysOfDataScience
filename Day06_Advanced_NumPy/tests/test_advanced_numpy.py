"""
Unit Tests

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 06
"""

import unittest
import numpy as np

from src.advanced_numpy import (
    create_copy,
    create_view,
    broadcast_add,
    broadcast_multiply,
    fancy_index,
    filter_greater_than,
    filter_between,
    create_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose_matrix,
    inverse_matrix,
    determinant,
    dot_product,
    cross_product,
    eigen_values,
    eigen_vectors,
)


class TestAdvancedNumPy(unittest.TestCase):

    def setUp(self):

        self.array = np.array([10, 20, 30, 40, 50])

        self.matrix1 = np.array([
            [1, 2],
            [3, 4]
        ])

        self.matrix2 = np.array([
            [5, 6],
            [7, 8]
        ])

    # ======================================================
    # COPY & VIEW
    # ======================================================

    def test_create_copy(self):

        copied = create_copy(self.array)

        self.assertTrue(
            np.array_equal(copied, self.array)
        )

    def test_create_view(self):

        viewed = create_view(self.array)

        self.assertTrue(
            np.shares_memory(
                viewed,
                self.array,
            )
        )

    # ======================================================
    # BROADCASTING
    # ======================================================

    def test_broadcast_add(self):

        expected = np.array(
            [15, 25, 35, 45, 55]
        )

        np.testing.assert_array_equal(
            broadcast_add(
                self.array,
                5,
            ),
            expected,
        )

    def test_broadcast_multiply(self):

        expected = np.array(
            [20, 40, 60, 80, 100]
        )

        np.testing.assert_array_equal(
            broadcast_multiply(
                self.array,
                2,
            ),
            expected,
        )

    # ======================================================
    # FANCY INDEXING
    # ======================================================

    def test_fancy_index(self):

        expected = np.array(
            [10, 30, 50]
        )

        np.testing.assert_array_equal(
            fancy_index(
                self.array,
                [0, 2, 4],
            ),
            expected,
        )

    # ======================================================
    # BOOLEAN MASKING
    # ======================================================

    def test_filter_greater_than(self):

        expected = np.array(
            [40, 50]
        )

        np.testing.assert_array_equal(
            filter_greater_than(
                self.array,
                35,
            ),
            expected,
        )

    def test_filter_between(self):

        expected = np.array(
            [20, 30, 40]
        )

        np.testing.assert_array_equal(
            filter_between(
                self.array,
                20,
                40,
            ),
            expected,
        )

    # ======================================================
    # MATRIX OPERATIONS
    # ======================================================

    def test_matrix_addition(self):

        expected = np.array([
            [6, 8],
            [10, 12]
        ])

        np.testing.assert_array_equal(
            add_matrices(
                self.matrix1,
                self.matrix2,
            ),
            expected,
        )

    def test_matrix_subtraction(self):

        expected = np.array([
            [4, 4],
            [4, 4]
        ])

        np.testing.assert_array_equal(
            subtract_matrices(
                self.matrix2,
                self.matrix1,
            ),
            expected,
        )

    def test_matrix_multiplication(self):

        expected = np.array([
            [19, 22],
            [43, 50]
        ])

        np.testing.assert_array_equal(
            multiply_matrices(
                self.matrix1,
                self.matrix2,
            ),
            expected,
        )

    def test_transpose(self):

        expected = np.array([
            [1, 3],
            [2, 4]
        ])

        np.testing.assert_array_equal(
            transpose_matrix(
                self.matrix1,
            ),
            expected,
        )

    def test_inverse(self):

        inverse = inverse_matrix(
            self.matrix1,
        )

        identity = np.matmul(
            self.matrix1,
            inverse,
        )

        np.testing.assert_array_almost_equal(
            identity,
            np.eye(2),
        )

    def test_determinant(self):

        self.assertAlmostEqual(
            determinant(self.matrix1),
            -2.0,
            places=6,
        )

    # ======================================================
    # LINEAR ALGEBRA
    # ======================================================

    def test_dot_product(self):

        self.assertEqual(
            dot_product(
                np.array([1, 2, 3]),
                np.array([4, 5, 6]),
            ),
            32,
        )

    def test_cross_product(self):

        expected = np.array(
            [-3, 6, -3]
        )

        np.testing.assert_array_equal(
            cross_product(
                np.array([1, 2, 3]),
                np.array([4, 5, 6]),
            ),
            expected,
        )

    def test_eigen_values(self):

        values = eigen_values(
            self.matrix1
        )

        self.assertEqual(
            len(values),
            2,
        )

    def test_eigen_vectors(self):

        vectors = eigen_vectors(
            self.matrix1
        )

        self.assertEqual(
            vectors.shape,
            (2, 2),
        )


if __name__ == "__main__":
    unittest.main()