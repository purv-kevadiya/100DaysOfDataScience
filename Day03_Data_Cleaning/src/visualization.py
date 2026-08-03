"""
Visualization Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 03

This module contains reusable visualization
functions for the cleaned dataset.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ==========================================================
# COMMON STYLE
# ==========================================================

sns.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (10, 6)

plt.rcParams["figure.dpi"] = 120

# ==========================================================
# SAVE CHART
# ==========================================================

def save_chart(
    output_path: Path,
) -> None:
    """
    Save current chart.

    Args:
        output_path: Chart file path.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        bbox_inches="tight",
    )

    plt.close()

# ==========================================================
# SALARY DISTRIBUTION
# ==========================================================

def salary_distribution(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot salary distribution.

    Args:
        df: Input DataFrame.
        output_path: Output image path.
    """

    plt.figure()

    sns.histplot(
        data=df,
        x="Salary",
        bins=10,
        kde=True,
    )

    plt.title("Salary Distribution")

    plt.xlabel("Salary")

    plt.ylabel("Employees")

    save_chart(output_path)

# ==========================================================
# DEPARTMENT COUNT
# ==========================================================

def department_count(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot department-wise employee count.
    """

    plt.figure()

    sns.countplot(
        data=df,
        x="Department",
    )

    plt.title("Employees by Department")

    plt.xlabel("Department")

    plt.ylabel("Count")

    save_chart(output_path)

# ==========================================================
# AGE DISTRIBUTION
# ==========================================================

def age_distribution(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot age distribution.

    Args:
        df: Input DataFrame.
        output_path: Output image path.
    """

    plt.figure()

    sns.histplot(
        data=df,
        x="Age",
        bins=8,
        kde=True,
    )

    plt.title("Age Distribution")

    plt.xlabel("Age")

    plt.ylabel("Employees")

    save_chart(output_path)

# ==========================================================
# PERFORMANCE DISTRIBUTION
# ==========================================================

def performance_distribution(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot employee performance distribution.

    Args:
        df: Input DataFrame.
        output_path: Output image path.
    """

    plt.figure()

    sns.countplot(
        data=df,
        x="Performance",
        order=["Poor", "Average", "Good", "Excellent"],
    )

    plt.title("Employee Performance")

    plt.xlabel("Performance")

    plt.ylabel("Employees")

    save_chart(output_path)

# ==========================================================
# SALARY BOXPLOT
# ==========================================================

def salary_boxplot(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot salary boxplot.

    Args:
        df: Input DataFrame.
        output_path: Output image path.
    """

    plt.figure()

    sns.boxplot(
        data=df,
        y="Salary",
    )

    plt.title("Salary Box Plot")

    plt.ylabel("Salary")

    save_chart(output_path)

# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

def correlation_heatmap(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot correlation heatmap.

    Args:
        df: Input DataFrame.
        output_path: Output image path.
    """

    plt.figure(figsize=(8, 6))

    numeric_df = df.select_dtypes(include="number")

    correlation = numeric_df.corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap="Blues",
        linewidths=0.5,
    )

    plt.title("Correlation Heatmap")

    save_chart(output_path)