"""
------------------------------------------------------------
Project    : Day 02 - E-Commerce Sales Data Analysis
Author     : Purv Kevadiya
Challenge  : #100DaysOfDataScience
Day        : 02

Description:
This program performs Exploratory Data Analysis (EDA)
on an e-commerce sales dataset using Pandas.
------------------------------------------------------------
"""

from pathlib import Path
import logging

import pandas as pd

from visualization import (
    category_revenue_bar_chart,
    sales_distribution_pie_chart,
    price_distribution_histogram,
    price_trend_line_chart,
    top_products_horizontal_bar_chart,
)

from config import (
    DATASET_FILE,
    CLEANED_DATA_FILE,
    CATEGORY_SUMMARY_FILE,
    STATISTICS_FILE,
    LOG_FILE,
    OUTPUT_FOLDER,
    CHART_FOLDER,
    REPORT_FOLDER,
    LOG_FOLDER,
    DISPLAY_MAX_COLUMNS,
    DISPLAY_WIDTH,
)

from helper import (
    create_directory,
    load_dataset,
    save_dataframe,
    save_text,
    print_title,
)


# ----------------------------------------------------------
# Configure Logging
# ----------------------------------------------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# ----------------------------------------------------------
# Create Required Folders
# ----------------------------------------------------------

def initialize_project() -> None:
    """Create required output folders."""

    create_directory(OUTPUT_FOLDER)
    create_directory(CHART_FOLDER)
    create_directory(REPORT_FOLDER)
    create_directory(LOG_FOLDER)


# ----------------------------------------------------------
# Explore Dataset
# ----------------------------------------------------------

def explore_dataset(df: pd.DataFrame) -> None:

    print_title("FIRST FIVE ROWS")
    print(df.head())

    print_title("LAST FIVE ROWS")
    print(df.tail())

    print_title("DATASET SHAPE")
    print(df.shape)

    print_title("COLUMN NAMES")
    print(df.columns)

    print_title("DATA TYPES")
    print(df.dtypes)

    print_title("DATASET INFORMATION")
    df.info()

    print_title("STATISTICAL SUMMARY")
    print(df.describe())


# ----------------------------------------------------------
# Perform Analysis
# ----------------------------------------------------------

def perform_analysis(df: pd.DataFrame) -> pd.DataFrame:

    print_title("PRODUCTS COSTING MORE THAN ₹1000")

    expensive_products = df[df["Price"] > 1000]

    print(expensive_products)

    print_title("SORT BY PRICE (DESCENDING)")

    sorted_df = df.sort_values(by="Price", ascending=False)

    print(sorted_df)

    df["Total"] = df["Price"] * df["Quantity"]

    df["Final_Price"] = (
        df["Total"] -
        (df["Total"] * df["Discount"] / 100)
    )

    print_title("UPDATED DATA")

    print(df)

    return df


# ----------------------------------------------------------
# Category Summary
# ----------------------------------------------------------

def category_summary(df: pd.DataFrame) -> pd.DataFrame:

    summary = (
        df.groupby("Category")[["Total", "Final_Price"]]
        .sum()
        .sort_values(by="Final_Price", ascending=False)
    )

    print_title("CATEGORY SUMMARY")

    print(summary)

    return summary


# ----------------------------------------------------------
# Save Reports
# ----------------------------------------------------------

def export_files(
    df: pd.DataFrame,
    summary: pd.DataFrame,
) -> None:

    save_dataframe(df, CLEANED_DATA_FILE)

    save_dataframe(summary, CATEGORY_SUMMARY_FILE)

    statistics = df.describe().to_string()

    save_text(statistics, STATISTICS_FILE)


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------

def main():

    pd.set_option("display.max_columns", DISPLAY_MAX_COLUMNS)

    pd.set_option("display.width", DISPLAY_WIDTH)

    initialize_project()

    logger.info("Application Started")

    try:

        df = load_dataset(DATASET_FILE)

        logger.info("Dataset Loaded Successfully")

        explore_dataset(df)

        updated_df = perform_analysis(df)

        summary = category_summary(updated_df)

        category_revenue_bar_chart(summary)

        sales_distribution_pie_chart(summary)

        price_distribution_histogram(updated_df)

        price_trend_line_chart(updated_df)

        top_products_horizontal_bar_chart(updated_df)

        export_files(updated_df, summary)

        logger.info("Analysis Completed Successfully")

        print_title("PROJECT COMPLETED SUCCESSFULLY")

    except Exception as error:

        logger.exception(error)

        print(error)


# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":

    main()