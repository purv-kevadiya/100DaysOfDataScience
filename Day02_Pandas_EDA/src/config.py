"""
------------------------------------------------------------
Project    : Day 02 - E-Commerce Sales Data Analysis
Author     : Purv Kevadiya
Challenge  : #100DaysOfDataScience
Day        : 02

Description:
Project configuration file.
Stores all project paths and constants in one place.
------------------------------------------------------------
"""

from pathlib import Path

# ----------------------------------------------------------
# Base Directories
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_ROOT / "data"

OUTPUT_FOLDER = PROJECT_ROOT / "outputs"

CHART_FOLDER = OUTPUT_FOLDER / "charts"

REPORT_FOLDER = OUTPUT_FOLDER / "reports"

LOG_FOLDER = PROJECT_ROOT / "logs"

# ----------------------------------------------------------
# Input Files
# ----------------------------------------------------------

DATASET_FILE = DATA_FOLDER / "ecommerce_sales.csv"

# ----------------------------------------------------------
# Output Files
# ----------------------------------------------------------

CLEANED_DATA_FILE = OUTPUT_FOLDER / "cleaned_data.csv"

CATEGORY_SUMMARY_FILE = OUTPUT_FOLDER / "category_summary.csv"

STATISTICS_FILE = OUTPUT_FOLDER / "statistics.txt"

LOG_FILE = LOG_FOLDER / "app.log"

# ----------------------------------------------------------
# Application Settings
# ----------------------------------------------------------

DISPLAY_MAX_COLUMNS = None

DISPLAY_WIDTH = 150

# ----------------------------------------------------------
# Chart Output Files
# ----------------------------------------------------------

BAR_CHART_FILE = CHART_FOLDER / "category_revenue_bar_chart.png"

PIE_CHART_FILE = CHART_FOLDER / "sales_distribution_pie_chart.png"

HISTOGRAM_FILE = CHART_FOLDER / "price_distribution_histogram.png"

LINE_CHART_FILE = CHART_FOLDER / "price_trend_line_chart.png"

HORIZONTAL_BAR_FILE = CHART_FOLDER / "top_products_horizontal_bar_chart.png"