"""
Report Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 03

This module generates professional text reports
for the cleaned dataset.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


# ==========================================================
# INTERNAL UTILITY
# ==========================================================

def create_output_directory(output_file: Path) -> None:
    """
    Create output directory if it does not exist.

    Args:
        output_file: Report file path.
    """

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )


# ==========================================================
# SUMMARY REPORT
# ==========================================================

def write_summary_report(
    df: pd.DataFrame,
    output_file: Path,
) -> None:
    """
    Generate dataset summary report.

    Args:
        df: Input DataFrame.
        output_file: Output report path.
    """

    create_output_directory(output_file)

    with open(output_file, "w", encoding="utf-8") as file:

        file.write("DAY 03 - DATA CLEANING SUMMARY REPORT\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            f"Generated On : "
            f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
        )

        # --------------------------------------------------

        file.write("DATASET OVERVIEW\n")
        file.write("-" * 70 + "\n")

        file.write(f"Rows    : {df.shape[0]}\n")
        file.write(f"Columns : {df.shape[1]}\n\n")

        # --------------------------------------------------

        file.write("COLUMN NAMES\n")
        file.write("-" * 70 + "\n")

        for column in df.columns:
            file.write(f"- {column}\n")

        file.write("\n")

        # --------------------------------------------------

        file.write("DATA TYPES\n")
        file.write("-" * 70 + "\n")

        file.write(df.dtypes.to_string())

        file.write("\n\n")

        # --------------------------------------------------

        file.write("MISSING VALUES\n")
        file.write("-" * 70 + "\n")

        missing = df.isnull().sum()

        for column, value in missing.items():
            file.write(f"{column:<20} : {value}\n")

        file.write("\n")

        # --------------------------------------------------

        duplicate_count = df.duplicated().sum()

        file.write("DUPLICATE ROWS\n")
        file.write("-" * 70 + "\n")

        file.write(f"Duplicate Rows : {duplicate_count}\n\n")

        # --------------------------------------------------

        memory = df.memory_usage(deep=True).sum() / 1024

        file.write("MEMORY USAGE\n")
        file.write("-" * 70 + "\n")

        file.write(f"{memory:.2f} KB\n")


# ==========================================================
# STATISTICS REPORT
# ==========================================================

def write_statistics_report(
    df: pd.DataFrame,
    output_file: Path,
) -> None:
    """
    Generate descriptive statistics report.

    Args:
        df: Input DataFrame.
        output_file: Output report path.
    """

    create_output_directory(output_file)

    with open(output_file, "w", encoding="utf-8") as file:

        file.write("DAY 03 - DATASET STATISTICS REPORT\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            f"Generated On : "
            f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
        )

        file.write("DESCRIPTIVE STATISTICS\n")
        file.write("-" * 70 + "\n")

        file.write(df.describe(include="all").to_string())

        file.write("\n\n")

        file.write("COLUMN DATA TYPES\n")
        file.write("-" * 70 + "\n")

        file.write(df.dtypes.to_string())

        file.write("\n\n")

        memory = df.memory_usage(deep=True).sum() / 1024

        file.write("MEMORY USAGE\n")
        file.write("-" * 70 + "\n")

        file.write(f"{memory:.2f} KB\n")


# ==========================================================
# CLEANING REPORT
# ==========================================================

def write_cleaning_report(
    original_rows: int,
    final_rows: int,
    output_file: Path,
) -> None:
    """
    Generate cleaning process report.

    Args:
        original_rows: Original dataset rows.
        final_rows: Final dataset rows.
        output_file: Output report path.
    """

    create_output_directory(output_file)

    removed_rows = original_rows - final_rows

    with open(output_file, "w", encoding="utf-8") as file:

        file.write("DAY 03 - DATA CLEANING REPORT\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            f"Generated On : "
            f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
        )

        file.write("CLEANING SUMMARY\n")
        file.write("-" * 70 + "\n")

        file.write(f"Original Rows : {original_rows}\n")
        file.write(f"Final Rows    : {final_rows}\n")
        file.write(f"Rows Removed  : {removed_rows}\n\n")

        file.write("OPERATIONS PERFORMED\n")
        file.write("-" * 70 + "\n")

        file.write("✓ Missing values handled\n")
        file.write("✓ Duplicate rows removed\n")
        file.write("✓ Text columns cleaned\n")
        file.write("✓ Data types converted\n")
        file.write("✓ Invalid values validated\n")
        file.write("✓ Salary outliers capped\n")

        file.write("\n")

        file.write("STATUS\n")
        file.write("-" * 70 + "\n")

        file.write("Data Cleaning Completed Successfully.\n")