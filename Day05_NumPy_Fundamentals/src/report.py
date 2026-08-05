"""
Report Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 05

Generate professional reports for NumPy operations.
"""

from pathlib import Path

import numpy as np


# ==========================================================
# ARRAY SUMMARY REPORT
# ==========================================================

def write_summary_report(
    array: np.ndarray,
    output_file: Path,
) -> None:
    """
    Generate array summary report.
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

        file.write("DAY 05 - NUMPY SUMMARY REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Shape       : {array.shape}\n")
        file.write(f"Dimensions  : {array.ndim}\n")
        file.write(f"Size        : {array.size}\n")
        file.write(f"Data Type   : {array.dtype}\n")
        file.write(f"Item Size   : {array.itemsize} bytes\n")
        file.write(f"Memory      : {array.nbytes} bytes\n\n")

        file.write("ARRAY DATA\n")
        file.write("-" * 60 + "\n")

        file.write(str(array))

# ==========================================================
# STATISTICS REPORT
# ==========================================================

def write_statistics_report(
    array: np.ndarray,
    output_file: Path,
) -> None:
    """
    Generate statistics report.
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

        file.write("DAY 05 - ARRAY STATISTICS\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Mean               : {np.mean(array)}\n")
        file.write(f"Median             : {np.median(array)}\n")
        file.write(f"Minimum            : {np.min(array)}\n")
        file.write(f"Maximum            : {np.max(array)}\n")
        file.write(f"Standard Deviation : {np.std(array)}\n")
        file.write(f"Variance           : {np.var(array)}\n")
        file.write(f"Total              : {np.sum(array)}\n")

# ==========================================================
# OPERATIONS REPORT
# ==========================================================

def write_operations_report(
    array: np.ndarray,
    output_file: Path,
) -> None:
    """
    Generate NumPy operations report.
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

        file.write("DAY 05 - NUMPY OPERATIONS REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write("Original Array\n")
        file.write("-" * 60 + "\n")
        file.write(str(array))
        file.write("\n\n")

        file.write("Sorted Array\n")
        file.write("-" * 60 + "\n")
        file.write(str(np.sort(array)))
        file.write("\n\n")

        file.write("Squared Array\n")
        file.write("-" * 60 + "\n")
        file.write(str(np.square(array)))
        file.write("\n\n")

        file.write("Square Root\n")
        file.write("-" * 60 + "\n")
        file.write(str(np.sqrt(array)))