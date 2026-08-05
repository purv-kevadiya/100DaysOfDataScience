"""
Configuration Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 05

Central configuration for Day 05 project.
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

RAW_DATA = DATA_DIR / "sample_data.csv"

# ==========================================================
# OUTPUT DIRECTORIES
# ==========================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

ARRAY_DIR = OUTPUT_DIR / "arrays"

REPORT_DIR = OUTPUT_DIR / "reports"

ARRAY_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# REPORT FILES
# ==========================================================

SUMMARY_REPORT = REPORT_DIR / "summary_report.txt"

STATISTICS_REPORT = REPORT_DIR / "statistics_report.txt"

OPERATIONS_REPORT = REPORT_DIR / "operations_report.txt"

# ==========================================================
# RANDOM SETTINGS
# ==========================================================

RANDOM_STATE = 42