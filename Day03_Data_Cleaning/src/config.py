"""
Configuration Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 03

This module contains all configuration variables,
file paths and application constants.
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
# OUTPUT DIRECTORIES
# ==========================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

CHART_DIR = OUTPUT_DIR / "charts"

REPORT_DIR = OUTPUT_DIR / "reports"

# ==========================================================
# LOG DIRECTORY
# ==========================================================

LOG_DIR = PROJECT_ROOT / "logs"

# ==========================================================
# RAW DATA FILE
# ==========================================================

RAW_DATA = RAW_DATA_DIR / "employee_data.csv"

# ==========================================================
# CLEAN DATA FILE
# ==========================================================

PROCESSED_DATA = PROCESSED_DATA_DIR / "employee_data_cleaned.csv"

# ==========================================================
# REPORT FILES
# ==========================================================

SUMMARY_REPORT = REPORT_DIR / "summary_report.txt"

STATISTICS_REPORT = REPORT_DIR / "statistics_report.txt"

# ==========================================================
# LOG FILE
# ==========================================================

LOG_FILE = LOG_DIR / "app.log"

# ==========================================================
# APPLICATION SETTINGS
# ==========================================================

DISPLAY_ROWS = 10

DISPLAY_COLUMNS = None

RANDOM_STATE = 42