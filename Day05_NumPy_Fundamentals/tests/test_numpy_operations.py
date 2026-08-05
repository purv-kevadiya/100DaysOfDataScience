"""
Unit Tests

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 05

Unit tests for NumPy operations.
"""

import unittest
import numpy as np

from src.numpy_operations import (
    create_array,
    create_zeros,
    create_ones,
    create_identity,
    reshape_array,
    transpose_array,
    mean,
    median,
    minimum,
    maximum,
    standard_deviation,
    variance,
    total,
    sort_array,
    filter_greater_than,
)


class TestNumPyOperations(unittest.TestCase):
    """
    Unit tests for NumPy operations.
    """

    def setUp(self):
        """
        Create sample arrays.
        """

        self.array = np.array(
            [10, 20, 30, 40, 50]
        )

        self.matrix = np.arange(
            1,
            10
        )

    # ======================================================
    # ARRAY CREATION
    # ======================================================

    def test_create_array(self):

        result = create_array(
            [10, 20, 30]
        )

        self.assertTrue(
            isinstance(result, np.ndarray)
        )

        np.testing.assert_array_equal(
            result,
            np.array([10, 20, 30])
        )

    def test_create_zeros(self):

        result = create_zeros((2, 2))

        expected = np.zeros((2, 2))

        np.testing.assert_array_equal(
            result,
            expected
        )

    def test_create_ones(self):

        result = create_ones((2, 2))

        expected = np.ones((2, 2))

        np.testing.assert_array_equal(
            result,
            expected
        )

    def test_identity(self):

        result = create_identity(3)

        expected = np.eye(3)

        np.testing.assert_array_equal(
            result,
            expected
        )

    # ======================================================
    # RESHAPE
    # ======================================================

    def test_reshape(self):

        reshaped = reshape_array(
            self.matrix,
            3,
            3
        )

        self.assertEqual(
            reshaped.shape,
            (3, 3)
        )

    def test_transpose(self):

        matrix = reshape_array(
            self.matrix,
            3,
            3
        )

        transposed = transpose_array(matrix)

        self.assertEqual(
            transposed.shape,
            (3, 3)
        )

    # ======================================================
    # STATISTICS
    # ======================================================

    def test_mean(self):

        self.assertEqual(
            mean(self.array),
            30
        )

    def test_median(self):

        self.assertEqual(
            median(self.array),
            30
        )

    def test_minimum(self):

        self.assertEqual(
            minimum(self.array),
            10
        )

    def test_maximum(self):

        self.assertEqual(
            maximum(self.array),
            50
        )

    def test_std(self):

        self.assertAlmostEqual(
            standard_deviation(self.array),
            np.std(self.array)
        )

    def test_variance(self):

        self.assertAlmostEqual(
            variance(self.array),
            np.var(self.array)
        )

    def test_total(self):

        self.assertEqual(
            total(self.array),
            150
        )

    # ======================================================
    # SORTING
    # ======================================================

    def test_sort(self):

        array = np.array(
            [45, 12, 67, 4]
        )

        expected = np.array(
            [4, 12, 45, 67]
        )

        np.testing.assert_array_equal(
            sort_array(array),
            expected
        )

    # ======================================================
    # FILTERING
    # ======================================================

    def test_filter(self):

        result = filter_greater_than(
            self.array,
            25
        )

        expected = np.array(
            [30, 40, 50]
        )

        np.testing.assert_array_equal(
            result,
            expected
        )


if __name__ == "__main__":
    unittest.main()