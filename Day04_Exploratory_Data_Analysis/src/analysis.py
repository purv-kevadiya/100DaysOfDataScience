"""
Analysis Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 04

This module contains reusable functions for
Exploratory Data Analysis (EDA).
"""

import pandas as pd


# ==========================================================
# DATASET LOADING
# ==========================================================

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load CSV dataset.

    Args:
        file_path: Path to CSV file.

    Returns:
        Loaded DataFrame.
    """

    return pd.read_csv(file_path)


# ==========================================================
# DATASET OVERVIEW
# ==========================================================

def dataset_overview(df: pd.DataFrame) -> None:
    """
    Display dataset overview.
    """

    print(df.head())

    print("\nDataset Information")
    print("-" * 60)
    df.info()


# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

def descriptive_statistics(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return descriptive statistics.
    """

    return df.describe(include="all")


# ==========================================================
# NUMERICAL ANALYSIS
# ==========================================================

def numerical_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return summary of numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    return pd.DataFrame({

        "Mean": numeric_df.mean(),

        "Median": numeric_df.median(),

        "Mode": numeric_df.mode().iloc[0],

        "Minimum": numeric_df.min(),

        "Maximum": numeric_df.max(),

        "Standard Deviation":
            numeric_df.std(),

        "Variance":
            numeric_df.var(),

        "Skewness":
            numeric_df.skew(),

        "Kurtosis":
            numeric_df.kurt(),

    })


# ==========================================================
# CATEGORICAL ANALYSIS
# ==========================================================

def categorical_summary(
    df: pd.DataFrame,
    column: str,
) -> pd.DataFrame:
    """
    Return frequency table.
    """

    summary = pd.DataFrame({

        "Count":
            df[column].value_counts(),

        "Percentage (%)":
            (
                df[column]
                .value_counts(normalize=True)
                * 100
            ).round(2)

    })

    return summary


# ==========================================================
# UNIQUE VALUES
# ==========================================================

def unique_values(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return unique value count.
    """

    return pd.DataFrame({

        "Unique Values":
            df.nunique()

    })


# ==========================================================
# CORRELATION
# ==========================================================

def correlation_matrix(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return correlation matrix.
    """

    return df.corr(numeric_only=True)


# ==========================================================
# GROUP ANALYSIS
# ==========================================================

def average_salary_by_department(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Average salary by department.
    """

    return (
        df.groupby("Department")["Salary"]
        .mean()
        .sort_values(ascending=False)
        .to_frame("Average Salary")
    )


def average_salary_by_city(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Average salary by city.
    """

    return (
        df.groupby("City")["Salary"]
        .mean()
        .sort_values(ascending=False)
        .to_frame("Average Salary")
    )


def average_salary_by_performance(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Average salary by performance.
    """

    return (
        df.groupby("Performance")["Salary"]
        .mean()
        .sort_values(ascending=False)
        .to_frame("Average Salary")
    )


# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

def highest_paid_department(
    df: pd.DataFrame,
):
    """
    Return highest paying department.
    """

    salary = average_salary_by_department(df)

    return salary.idxmax()[0]


def highest_paid_city(
    df: pd.DataFrame,
):
    """
    Return highest paying city.
    """

    salary = average_salary_by_city(df)

    return salary.idxmax()[0]


def total_employees(
    df: pd.DataFrame,
) -> int:
    """
    Total employees.
    """

    return len(df)


def total_departments(
    df: pd.DataFrame,
) -> int:
    """
    Total departments.
    """

    return df["Department"].nunique()


def average_salary(
    df: pd.DataFrame,
) -> float:
    """
    Overall average salary.
    """

    return round(df["Salary"].mean(), 2)


def average_age(
    df: pd.DataFrame,
) -> float:
    """
    Overall average age.
    """

    return round(df["Age"].mean(), 2)