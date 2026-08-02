"""
------------------------------------------------------------
Project    : Day 02 - E-Commerce Sales Data Analysis
Author     : Purv Kevadiya
Challenge  : #100DaysOfDataScience
Day        : 02

Description:
Visualization functions using Matplotlib.
------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import pandas as pd

from config import (
    BAR_CHART_FILE,
    PIE_CHART_FILE,
    HISTOGRAM_FILE,
    LINE_CHART_FILE,
    HORIZONTAL_BAR_FILE,
)


def category_revenue_bar_chart(summary: pd.DataFrame) -> None:
    """Generate a bar chart for category revenue."""

    plt.figure(figsize=(10, 6))

    plt.bar(summary.index, summary["Final_Price"])

    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue (₹)")

    plt.tight_layout()

    plt.savefig(BAR_CHART_FILE, dpi=300)

    plt.close()


def sales_distribution_pie_chart(summary: pd.DataFrame) -> None:
    """Generate a pie chart for sales distribution."""

    plt.figure(figsize=(8, 8))

    plt.pie(
        summary["Final_Price"],
        labels=summary.index,
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("Sales Distribution by Category")

    plt.tight_layout()

    plt.savefig(PIE_CHART_FILE, dpi=300)

    plt.close()


def price_distribution_histogram(df: pd.DataFrame) -> None:
    """Generate a histogram of product prices."""

    plt.figure(figsize=(10, 6))

    plt.hist(df["Price"], bins=5)

    plt.title("Price Distribution")
    plt.xlabel("Price (₹)")
    plt.ylabel("Number of Products")

    plt.tight_layout()

    plt.savefig(HISTOGRAM_FILE, dpi=300)

    plt.close()


def price_trend_line_chart(df: pd.DataFrame) -> None:
    """Generate a line chart for product prices."""

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["Order_ID"],
        df["Price"],
        marker="o",
    )

    plt.title("Price Trend by Order")
    plt.xlabel("Order ID")
    plt.ylabel("Price (₹)")

    plt.tight_layout()

    plt.savefig(LINE_CHART_FILE, dpi=300)

    plt.close()


def top_products_horizontal_bar_chart(df: pd.DataFrame) -> None:
    """Generate a horizontal bar chart for product revenue."""

    top_products = (
        df.sort_values("Final_Price", ascending=False)
        .head(5)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        top_products["Product"],
        top_products["Final_Price"],
    )

    plt.title("Top 5 Products by Revenue")
    plt.xlabel("Revenue (₹)")
    plt.ylabel("Product")

    plt.tight_layout()

    plt.savefig(HORIZONTAL_BAR_FILE, dpi=300)

    plt.close()