"""
Helper Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 06

Reusable helper functions for displaying
formatted output throughout the project.
"""

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
# PRINT SUB HEADING
# ==========================================================

def print_sub_heading(title: str) -> None:
    """
    Print formatted subsection heading.
    """

    line = "-" * 60

    print(f"\n{line}")
    print(title)
    print(line)


# ==========================================================
# DISPLAY ARRAY
# ==========================================================

def display_array(
    title: str,
    array: np.ndarray,
) -> None:
    """
    Display NumPy array with heading.

    Args:
        title: Array title.
        array: NumPy array.
    """

    print_heading(title)
    print(array)


# ==========================================================
# ARRAY INFORMATION
# ==========================================================

def array_information(
    array: np.ndarray,
) -> None:
    """
    Display array properties.

    Args:
        array: NumPy array.
    """

    print(f"Shape      : {array.shape}")
    print(f"Dimensions : {array.ndim}")
    print(f"Size       : {array.size}")
    print(f"Data Type  : {array.dtype}")
    print(f"Item Size  : {array.itemsize} bytes")
    print(f"Memory     : {array.nbytes} bytes")


# ==========================================================
# SUCCESS MESSAGE
# ==========================================================

def success(message: str) -> None:
    """
    Print success message.
    """

    print(f"✓ {message}")


# ==========================================================
# SEPARATOR
# ==========================================================

def separator() -> None:
    """
    Print separator line.
    """

    print("-" * 60)