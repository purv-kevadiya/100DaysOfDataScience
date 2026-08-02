"""
------------------------------------------------------------
Project    : Day 02 - E-Commerce Sales Data Analysis
Author     : Purv Kevadiya
Challenge  : #100DaysOfDataScience
Day        : 02

Description:
Reusable helper functions.
------------------------------------------------------------
"""

from pathlib import Path
import pandas as pd


def create_directory(directory: Path) -> None:
    """
    Create a directory if it does not already exist.
    """
    directory.mkdir(parents=True, exist_ok=True)


def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Load dataset from CSV file.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    DataFrame
    """
    return pd.read_csv(file_path)


def save_dataframe(df: pd.DataFrame, file_path: Path) -> None:
    """
    Save DataFrame into CSV.
    """
    df.to_csv(file_path, index=False)


def save_text(text: str, file_path: Path) -> None:
    """
    Save text into file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)


def print_title(title: str) -> None:
    """
    Print beautiful console title.
    """

    print("\n" + "=" * 60)

    print(title)

    print("=" * 60)