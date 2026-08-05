"""
Helper Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 05

Reusable helper functions for NumPy projects.
"""

from pathlib import Path

import numpy as np


# ==========================================================
# PRINT HEADING
# ==========================================================

def print_heading(title: str) -> None:
    """
    Print formatted section heading.
    """

    line = "=" * 60

    print(f"\n{line}")
    print(title.upper())
    print(line)


# ==========================================================
# PRINT SEPARATOR
# ==========================================================

def print_separator() -> None:
    """
    Print separator line.
    """

    print("-" * 60)


# ==========================================================
# SAVE NUMPY ARRAY
# ==========================================================

def save_array(
    array: np.ndarray,
    output_file: Path,
) -> None:
    """
    Save NumPy array as .npy file.
    """

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    np.save(
        output_file,
        array,
    )


# ==========================================================
# SAVE TEXT REPORT
# ==========================================================

def save_text(
    text: str,
    output_file: Path,
) -> None:
    """
    Save text report.
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

        file.write(text)


# ==========================================================
# DISPLAY ARRAY INFO
# ==========================================================

def print_array_info(
    array: np.ndarray,
    title: str = "Array",
) -> None:
    """
    Display useful information about a NumPy array.
    """

    print_heading(title)

    print(array)

    print_separator()

    print(f"Shape      : {array.shape}")
    print(f"Dimensions : {array.ndim}")
    print(f"Size       : {array.size}")
    print(f"Data Type  : {array.dtype}")
    print(f"Item Size  : {array.itemsize} bytes")
    print(f"Memory     : {array.nbytes} bytes")