"""
Helper Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 03

This module contains reusable helper functions used
throughout the project.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


# ==========================================================
# CONSOLE UTILITIES
# ==========================================================

def print_heading(title: str) -> None:
    """
    Print a formatted section heading.

    Args:
        title: Heading text.
    """

    line = "=" * 60

    print(f"\n{line}")
    print(title.upper())
    print(line)


# ==========================================================
# DATASET UTILITIES
# ==========================================================

def dataset_shape(df: pd.DataFrame) -> None:
    """
    Display dataset dimensions.

    Args:
        df: Input DataFrame.
    """

    rows, columns = df.shape

    print(f"Rows    : {rows}")
    print(f"Columns : {columns}")


def dataset_info(df: pd.DataFrame) -> None:
    """
    Display dataset information.

    Args:
        df: Input DataFrame.
    """

    print(df.info())


def preview_dataset(df: pd.DataFrame, rows: int = 5) -> None:
    """
    Display first rows of dataset.

    Args:
        df: Input DataFrame.
        rows: Number of rows.
    """

    print(df.head(rows))


# ==========================================================
# MISSING VALUE REPORT
# ==========================================================

def missing_value_report(df: pd.DataFrame) -> None:
    """
    Display missing value report.

    Args:
        df: Input DataFrame.
    """

    report = pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Percentage (%)": (
            df.isnull().sum() / len(df) * 100
        ).round(2)
    })

    print(report)


# ==========================================================
# DUPLICATE REPORT
# ==========================================================

def duplicate_report(count: int) -> None:
    """
    Display duplicate report.

    Args:
        count: Duplicate row count.
    """

    print(f"Duplicate Rows Found : {count}")


# ==========================================================
# DATA TYPE REPORT
# ==========================================================

def data_type_report(df: pd.DataFrame) -> None:
    """
    Display data types.

    Args:
        df: Input DataFrame.
    """

    print(df.dtypes)


# ==========================================================
# FILE UTILITIES
# ==========================================================

def file_exists(file_path: Path) -> bool:
    """
    Check whether file exists.

    Args:
        file_path: File path.

    Returns:
        True if exists.
    """

    return file_path.exists()


# ==========================================================
# APPLICATION TIMER
# ==========================================================

def current_time() -> str:
    """
    Return current timestamp.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ==========================================================
# SUMMARY
# ==========================================================

def cleaning_summary(
    original_rows: int,
    final_rows: int
) -> None:
    """
    Display cleaning summary.

    Args:
        original_rows: Original dataset rows.
        final_rows: Final dataset rows.
    """

    removed = original_rows - final_rows

    print_heading("DATA CLEANING SUMMARY")

    print(f"Original Rows : {original_rows}")
    print(f"Final Rows    : {final_rows}")
    print(f"Rows Removed  : {removed}")

    print("\nCleaning completed successfully.")