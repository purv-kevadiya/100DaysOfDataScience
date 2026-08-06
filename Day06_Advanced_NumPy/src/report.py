"""
Report Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 06

Generate professional reports for
Advanced NumPy operations.
"""

from pathlib import Path

import numpy as np


# ==========================================================
# SUMMARY REPORT
# ==========================================================

def write_summary_report(
    output_file: Path,
) -> None:
    """
    Generate summary report.
    """

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "DAY 06 - ADVANCED NUMPY SUMMARY\n"
        )

        file.write("=" * 60)

        file.write("\n\n")

        file.write(
            "Topics Covered\n"
        )

        file.write("-" * 60)

        file.write("\n")

        topics = [

            "Copy vs View",

            "Broadcasting",

            "Fancy Indexing",

            "Boolean Masking",

            "Matrix Operations",

            "Linear Algebra",

            "Vectorization",

            "Performance Comparison",

        ]

        for topic in topics:

            file.write(f"• {topic}\n")

# ==========================================================
# ARRAY REPORT
# ==========================================================

def write_array_report(
    array: np.ndarray,
    output_file: Path,
) -> None:
    """
    Save array statistics.
    """

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        file.write("ARRAY REPORT\n")

        file.write("=" * 60)

        file.write("\n\n")

        file.write(f"Shape      : {array.shape}\n")

        file.write(f"Dimensions : {array.ndim}\n")

        file.write(f"Size       : {array.size}\n")

        file.write(f"Data Type  : {array.dtype}\n")

        file.write(f"Mean       : {np.mean(array)}\n")

        file.write(f"Minimum    : {np.min(array)}\n")

        file.write(f"Maximum    : {np.max(array)}\n")

        file.write(f"Std Dev    : {np.std(array)}\n")

# ==========================================================
# PERFORMANCE REPORT
# ==========================================================

def write_performance_report(
    result: dict,
    output_file: Path,
) -> None:
    """
    Save execution time report.
    """

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "PERFORMANCE REPORT\n"
        )

        file.write("=" * 60)

        file.write("\n\n")

        for key, value in result.items():

            file.write(
                f"{key:<20}: {value:.8f} sec\n"
            )