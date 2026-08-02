"""
------------------------------------------------------------
Project    : Day 02 - E-Commerce Sales Data Analysis
Author     : Purv Kevadiya
Challenge  : #100DaysOfDataScience
Day        : 02

Description:
Unit tests for helper functions.
------------------------------------------------------------
"""

import sys
import unittest
from pathlib import Path

import pandas as pd

# ----------------------------------------------------------
# Add src folder to Python path
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_FOLDER = PROJECT_ROOT / "src"

sys.path.append(str(SRC_FOLDER))

from helper import load_dataset, save_dataframe
from config import DATASET_FILE


class TestDataFunctions(unittest.TestCase):
    """Test helper functions."""

    def setUp(self):
        """Runs before each test."""
        self.dataset = load_dataset(DATASET_FILE)

    def test_dataset_is_dataframe(self):
        """Dataset should load as a DataFrame."""
        self.assertIsInstance(self.dataset, pd.DataFrame)

    def test_dataset_not_empty(self):
        """Dataset should contain rows."""
        self.assertGreater(len(self.dataset), 0)

    def test_required_columns_exist(self):
        """Check required columns."""

        expected_columns = {
            "Order_ID",
            "Customer",
            "Category",
            "Product",
            "Price",
            "Quantity",
            "Discount",
        }

        self.assertTrue(
            expected_columns.issubset(self.dataset.columns)
        )

    def test_price_column_numeric(self):
        """Price column should be numeric."""

        self.assertTrue(
            pd.api.types.is_numeric_dtype(
                self.dataset["Price"]
            )
        )

    def test_quantity_column_numeric(self):
        """Quantity column should be numeric."""

        self.assertTrue(
            pd.api.types.is_numeric_dtype(
                self.dataset["Quantity"]
            )
        )

    def test_save_dataframe(self):
        """Test CSV export."""

        output_file = PROJECT_ROOT / "outputs" / "test_output.csv"

        save_dataframe(self.dataset, output_file)

        self.assertTrue(output_file.exists())

        output_file.unlink()


if __name__ == "__main__":
    unittest.main(verbosity=2)