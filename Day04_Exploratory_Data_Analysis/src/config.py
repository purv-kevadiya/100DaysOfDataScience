"""
Configuration Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 04

This module contains all project configuration,
file paths and visualization settings.
"""

from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# DATA DIRECTORIES
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ==========================================================
# INPUT DATASET
# ==========================================================

PROCESSED_DATA = (
    PROCESSED_DATA_DIR /
    "employee_data_cleaned.csv"
)

# ==========================================================
# OUTPUT DIRECTORIES
# ==========================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

CHART_DIR = OUTPUT_DIR / "charts"

REPORT_DIR = OUTPUT_DIR / "reports"

# ==========================================================
# DATA FILES
# ==========================================================

DATA_FILE = (
    PROCESSED_DATA_DIR /
    "employee_data_cleaned.csv"
)

# ==========================================================
# APPLICATION SETTINGS
# ==========================================================

FIGURE_SIZE = (10, 6)

DPI = 300

STYLE = "ggplot"

RANDOM_STATE = 42

# ==========================================================
# MATPLOTLIB SETTINGS
# ==========================================================

FIGURE_SIZE = (10, 6)

DPI = 300

STYLE = "ggplot"