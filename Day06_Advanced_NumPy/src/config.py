"""
Configuration Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 06

Central configuration for the project.
"""

from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# DATA
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ==========================================================
# OUTPUTS
# ==========================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

ARRAY_DIR = OUTPUT_DIR / "arrays"

REPORT_DIR = OUTPUT_DIR / "reports"

SUMMARY_REPORT = REPORT_DIR / "summary_report.txt"

ARRAY_REPORT = REPORT_DIR / "array_report.txt"

PERFORMANCE_REPORT = REPORT_DIR / "performance_report.txt"

# ==========================================================
# RANDOM SEED
# ==========================================================

RANDOM_STATE = 42