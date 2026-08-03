"""
Data Cleaning Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 03

This module contains reusable data loading,
cleaning and preprocessing functions.
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
        Loaded pandas DataFrame.
    """

    return pd.read_csv(file_path)


# ==========================================================
# DATASET EXPLORATION
# ==========================================================

def basic_information(df: pd.DataFrame) -> None:
    """
    Display dataset overview.

    Args:
        df: Input DataFrame.
    """

    print(df.head())

    print("\nDataset Information")
    print("-" * 50)
    df.info()

    print("\nStatistical Summary")
    print("-" * 50)
    print(df.describe(include="all"))


# ==========================================================
# DATASET INFORMATION
# ==========================================================

def total_rows(df: pd.DataFrame) -> int:
    """
    Return total number of rows.
    """

    return df.shape[0]


def total_columns(df: pd.DataFrame) -> int:
    """
    Return total number of columns.
    """

    return df.shape[1]


def column_names(df: pd.DataFrame) -> list:
    """
    Return all column names.
    """

    return list(df.columns)


# ==========================================================
# DATA TYPES
# ==========================================================

def show_data_types(df: pd.DataFrame) -> None:
    """
    Display column data types.
    """

    print(df.dtypes)


# ==========================================================
# MEMORY USAGE
# ==========================================================

def memory_usage(df: pd.DataFrame) -> None:
    """
    Display dataset memory usage.
    """

    memory = df.memory_usage(deep=True).sum() / 1024

    print(f"Memory Usage : {memory:.2f} KB")

# ==========================================================
# MISSING VALUE HANDLING
# ==========================================================

def missing_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a summary of missing values.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame containing missing value count and percentage.
    """

    return pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Percentage (%)": (
            df.isnull().sum() / len(df) * 100
        ).round(2)
    })


def fill_salary_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing Salary values using the rounded mean.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    mean_salary = round(df["Salary"].mean(), 2)

    df["Salary"] = df["Salary"].fillna(mean_salary)

    return df


def fill_age_median(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing Age values using the median.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    median_age = df["Age"].median()

    df["Age"] = df["Age"].fillna(median_age)

    return df


def fill_performance_mode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing Performance values using the mode.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    mode_value = df["Performance"].mode()[0]

    df["Performance"] = df["Performance"].fillna(mode_value)

    return df

# ==========================================================
# DUPLICATE HANDLING
# ==========================================================

def check_duplicates(df: pd.DataFrame) -> int:
    """
    Count duplicate rows.

    Args:
        df: Input DataFrame.

    Returns:
        Total duplicate rows.
    """

    return df.duplicated().sum()


def show_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return duplicate rows.

    Args:
        df: Input DataFrame.

    Returns:
        Duplicate rows.
    """

    return df[df.duplicated()]


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame after removing duplicates.
    """

    return df.drop_duplicates().reset_index(drop=True)


def duplicate_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate duplicate report.

    Args:
        df: Input DataFrame.

    Returns:
        Duplicate summary.
    """

    duplicate_count = check_duplicates(df)

    return pd.DataFrame({
        "Duplicate Rows": [duplicate_count],
        "Status": [
            "Duplicates Found"
            if duplicate_count > 0
            else "No Duplicates"
        ]
    })

# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_name(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Name column.

    Operations:
    - Remove leading/trailing spaces
    - Remove multiple spaces
    - Convert to Title Case
    """

    df["Name"] = (
        df["Name"]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
    )

    return df


def clean_city(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean City column.

    Operations:
    - Remove leading/trailing spaces
    - Convert to Title Case
    """

    df["City"] = (
        df["City"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return df


def clean_department(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize Department names.
    """

    df["Department"] = (
        df["Department"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return df


def clean_performance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize Performance values.
    """

    df["Performance"] = (
        df["Performance"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return df

# ==========================================================
# DATA TYPE CONVERSION
# ==========================================================

def convert_joining_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert Joining_Date column to datetime format.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    df["Joining_Date"] = pd.to_datetime(
        df["Joining_Date"],
        errors="coerce"
    )

    return df


def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert numeric columns into numeric datatype.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    numeric_columns = [
        "Employee_ID",
        "Age",
        "Salary",
        "Experience"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df


def convert_category_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert text columns into category datatype.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    category_columns = [
        "Department",
        "City",
        "Performance"
    ]

    for column in category_columns:

        df[column] = df[column].astype("category")

    return df

# ==========================================================
# DATA VALIDATION
# ==========================================================

def fix_invalid_age(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace invalid Age values with the median age.

    Valid age range: 18 to 60 years.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    median_age = df.loc[
        df["Age"].between(18, 60),
        "Age"
    ].median()

    df.loc[
        ~df["Age"].between(18, 60),
        "Age"
    ] = median_age

    return df


def fix_negative_salary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace negative Salary values with the median salary.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    median_salary = df.loc[
        df["Salary"] >= 0,
        "Salary"
    ].median()

    df.loc[
        df["Salary"] < 0,
        "Salary"
    ] = median_salary

    return df


def fix_negative_experience(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace negative Experience values with zero.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    df.loc[
        df["Experience"] < 0,
        "Experience"
    ] = 0

    return df


def validate_joining_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows having invalid Joining_Date values.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    return (
        df
        .dropna(subset=["Joining_Date"])
        .reset_index(drop=True)
    )


def validation_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a validation summary report.

    Args:
        df: Input DataFrame.

    Returns:
        Validation summary DataFrame.
    """

    summary = {
        "Invalid Age": [
            (~df["Age"].between(18, 60)).sum()
        ],
        "Negative Salary": [
            (df["Salary"] < 0).sum()
        ],
        "Negative Experience": [
            (df["Experience"] < 0).sum()
        ],
        "Invalid Joining Date": [
            df["Joining_Date"].isna().sum()
        ]
    }

    return pd.DataFrame(summary)

# ==========================================================
# OUTLIER DETECTION
# ==========================================================

def detect_outliers_iqr(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:
    """
    Detect outliers using the IQR method.

    Args:
        df: Input DataFrame.
        column: Numeric column name.

    Returns:
        DataFrame containing outlier rows.
    """

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    return outliers.sort_values(
    by=column,
    ascending=False
)

def cap_salary_outliers(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Cap Salary outliers using IQR boundaries.

    Args:
        df: Input DataFrame.

    Returns:
        Updated DataFrame.
    """

    q1 = df["Salary"].quantile(0.25)
    q3 = df["Salary"].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    df["Salary"] = df["Salary"].clip(
        lower=lower_bound,
        upper=upper_bound
    )

    return df


def outlier_summary(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:
    """
    Generate outlier summary.

    Args:
        df: Input DataFrame.
        column: Numeric column.

    Returns:
        Summary DataFrame.
    """

    outliers = detect_outliers_iqr(
        df,
        column
    )

    return pd.DataFrame({
        "Column": [column],
        "Outliers": [len(outliers)]
    })