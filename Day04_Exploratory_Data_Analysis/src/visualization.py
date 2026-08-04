"""
Visualization Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 04

This module contains reusable visualization
functions for creating professional charts
using Matplotlib.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from config import (
    FIGURE_SIZE,
    DPI,
    STYLE,
)

from helper import save_chart

# ==========================================================
# DATASET LOADING
# ==========================================================

def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Load cleaned dataset.

    Args:
        file_path: CSV file path.

    Returns:
        Loaded DataFrame.
    """

    return pd.read_csv(file_path)

# ==========================================================
# MATPLOTLIB STYLE
# ==========================================================

plt.style.use(STYLE)

# ==========================================================
# LINE CHART
# ==========================================================

def plot_salary_line_chart(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Salary Line Chart.
    """

    plt.figure(figsize=FIGURE_SIZE)

    plt.plot(
        df["Employee_ID"],
        df["Salary"],
        marker="o",
        linewidth=2,
    )

    plt.title("Salary Trend")

    plt.xlabel("Employee ID")

    plt.ylabel("Salary")

    plt.grid(True)

    save_chart(output_path)

# ==========================================================
# BAR CHART
# ==========================================================

def plot_department_count(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Department Count.
    """

    plt.figure(figsize=FIGURE_SIZE)

    department = df["Department"].value_counts()

    plt.bar(
        department.index,
        department.values,
    )

    plt.title("Employees by Department")

    plt.xlabel("Department")

    plt.ylabel("Count")

    save_chart(output_path)

# ==========================================================
# HISTOGRAM
# ==========================================================

def plot_age_distribution(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Age Distribution.
    """

    plt.figure(figsize=FIGURE_SIZE)

    plt.hist(
        df["Age"],
        bins=8,
    )

    plt.title("Age Distribution")

    plt.xlabel("Age")

    plt.ylabel("Frequency")

    save_chart(output_path)

# ==========================================================
# SCATTER PLOT
# ==========================================================

def plot_experience_vs_salary(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Experience vs Salary.
    """

    plt.figure(figsize=FIGURE_SIZE)

    plt.scatter(
        df["Experience"],
        df["Salary"],
    )

    plt.title("Experience vs Salary")

    plt.xlabel("Experience")

    plt.ylabel("Salary")

    save_chart(output_path)

# ==========================================================
# PIE CHART
# ==========================================================

def plot_performance_distribution(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Performance Distribution.
    """

    plt.figure(figsize=(8, 8))

    performance = df["Performance"].value_counts()

    plt.pie(
        performance.values,
        labels=performance.index,
        autopct="%1.1f%%",
    )

    plt.title("Performance Distribution")

    save_chart(output_path)

# ==========================================================
# BOX PLOT
# ==========================================================

def plot_salary_boxplot(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Salary Boxplot.
    """

    plt.figure(figsize=FIGURE_SIZE)

    plt.boxplot(df["Salary"])

    plt.title("Salary Box Plot")

    plt.ylabel("Salary")

    save_chart(output_path)

# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

def plot_correlation_heatmap(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Correlation Heatmap.
    """

    plt.figure(figsize=(8, 6))

    correlation = df.corr(numeric_only=True)

    plt.imshow(
        correlation,
        cmap="coolwarm",
        interpolation="nearest",
    )

    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=45,
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns,
    )

    plt.title("Correlation Heatmap")

    save_chart(output_path)

# ==========================================================
# DASHBOARD
# ==========================================================

def plot_dashboard(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Create a professional dashboard using multiple subplots.

    Args:
        df: Input DataFrame.
        output_path: Output image path.
    """

    fig, axes = plt.subplots(
        2,
        2,
        figsize=(14, 10)
    )

    # ------------------------------------------------------
    # Salary Distribution
    # ------------------------------------------------------

    axes[0, 0].hist(
        df["Salary"],
        bins=8
    )

    axes[0, 0].set_title(
        "Salary Distribution"
    )

    axes[0, 0].set_xlabel(
        "Salary"
    )

    axes[0, 0].set_ylabel(
        "Frequency"
    )

    # ------------------------------------------------------
    # Department Count
    # ------------------------------------------------------

    department = df["Department"].value_counts()

    axes[0, 1].bar(
        department.index,
        department.values
    )

    axes[0, 1].set_title(
        "Department Count"
    )

    axes[0, 1].set_xlabel(
        "Department"
    )

    axes[0, 1].set_ylabel(
        "Employees"
    )

    # ------------------------------------------------------
    # Experience vs Salary
    # ------------------------------------------------------

    axes[1, 0].scatter(
        df["Experience"],
        df["Salary"]
    )

    axes[1, 0].set_title(
        "Experience vs Salary"
    )

    axes[1, 0].set_xlabel(
        "Experience"
    )

    axes[1, 0].set_ylabel(
        "Salary"
    )

    # ------------------------------------------------------
    # Performance Distribution
    # ------------------------------------------------------

    performance = df["Performance"].value_counts()

    axes[1, 1].pie(
        performance.values,
        labels=performance.index,
        autopct="%1.1f%%"
    )

    axes[1, 1].set_title(
        "Performance Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=DPI,
        bbox_inches="tight"
    )

    plt.close()