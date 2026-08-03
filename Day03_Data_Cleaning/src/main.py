"""
Day 03 - Professional Data Cleaning

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 03

This module serves as the entry point for the Day 03 project.

Workflow
--------
1. Dataset Loading
2. Dataset Exploration
3. Missing Value Handling
4. Duplicate Detection & Removal
5. Text Cleaning
6. Data Type Conversion
7. Data Validation
8. Outlier Detection & Treatment
9. Save Cleaned Dataset
10. Generate Reports
11. Generate Visualizations
12. Cleaning Summary
"""

from config import (
    RAW_DATA,
    PROCESSED_DATA,
    SUMMARY_REPORT,
    STATISTICS_REPORT,
    CHART_DIR,
)

from helper import (
    print_heading,
    dataset_shape,
    missing_value_report,
    cleaning_summary,
)

from cleaning import (
    load_dataset,
    basic_information,

    fill_salary_mean,
    fill_age_median,
    fill_performance_mode,

    check_duplicates,
    show_duplicates,
    remove_duplicates,
    duplicate_summary,

    clean_name,
    clean_city,
    clean_department,
    clean_performance,

    convert_joining_date,
    convert_numeric_columns,
    convert_category_columns,

    fix_invalid_age,
    fix_negative_salary,
    fix_negative_experience,
    validate_joining_date,
    validation_summary,

    detect_outliers_iqr,
    outlier_summary,
    cap_salary_outliers,
)

from report import (
    write_summary_report,
    write_statistics_report,
    write_cleaning_report,
)

from visualization import (
    salary_distribution,
    department_count,
    age_distribution,
    performance_distribution,
    salary_boxplot,
    correlation_heatmap,
)


def main() -> None:
    """
    Execute complete data cleaning workflow.
    """

    # ==========================================================
    # STEP 1 : LOAD DATASET
    # ==========================================================

    print_heading("DAY 03 - PROFESSIONAL DATA CLEANING")

    df = load_dataset(RAW_DATA)

    # ==========================================================
    # STEP 2 : DATASET OVERVIEW
    # ==========================================================

    print_heading("DATASET SHAPE")
    dataset_shape(df)

    print_heading("FIRST FIVE ROWS")
    basic_information(df)

    # ==========================================================
    # STEP 3 : MISSING VALUE REPORT
    # ==========================================================

    print_heading("MISSING VALUE REPORT")
    missing_value_report(df)

    # ==========================================================
    # STEP 4 : HANDLE MISSING VALUES
    # ==========================================================

    cleaned_df = df.copy()

    print_heading("FILLING MISSING VALUES")

    cleaned_df = fill_salary_mean(cleaned_df)
    cleaned_df = fill_age_median(cleaned_df)
    cleaned_df = fill_performance_mode(cleaned_df)

    print("✓ Missing values handled successfully.")

    # ==========================================================
    # STEP 5 : DUPLICATE REPORT
    # ==========================================================

    print_heading("DUPLICATE REPORT")
    print(duplicate_summary(cleaned_df))

    print_heading("DUPLICATE ROWS")

    duplicates = show_duplicates(cleaned_df)

    if duplicates.empty:
        print("No duplicate rows found.")
    else:
        print(duplicates)

    print_heading("REMOVE DUPLICATES")

    duplicate_count = check_duplicates(cleaned_df)

    cleaned_df = remove_duplicates(cleaned_df)

    print(f"✓ {duplicate_count} duplicate row(s) removed.")

    # ==========================================================
    # STEP 6 : TEXT CLEANING
    # ==========================================================

    print_heading("TEXT CLEANING")

    cleaned_df = clean_name(cleaned_df)
    cleaned_df = clean_city(cleaned_df)
    cleaned_df = clean_department(cleaned_df)
    cleaned_df = clean_performance(cleaned_df)

    print("✓ Text cleaned successfully.")

    # ==========================================================
    # STEP 7 : DATA TYPE CONVERSION
    # ==========================================================

    print_heading("DATA TYPE CONVERSION")

    cleaned_df = convert_joining_date(cleaned_df)
    cleaned_df = convert_numeric_columns(cleaned_df)
    cleaned_df = convert_category_columns(cleaned_df)

    print("✓ Data types converted successfully.")

    # ==========================================================
    # STEP 8 : DATA VALIDATION
    # ==========================================================

    print_heading("DATA VALIDATION")

    cleaned_df = fix_invalid_age(cleaned_df)
    cleaned_df = fix_negative_salary(cleaned_df)
    cleaned_df = fix_negative_experience(cleaned_df)
    cleaned_df = validate_joining_date(cleaned_df)

    print(validation_summary(cleaned_df))

    print("✓ Dataset validation completed.")

    # ==========================================================
    # STEP 9 : OUTLIER DETECTION
    # ==========================================================

    print_heading("OUTLIER REPORT")

    print(outlier_summary(cleaned_df, "Salary"))

    salary_outliers = detect_outliers_iqr(
        cleaned_df,
        "Salary",
    )

    if salary_outliers.empty:
        print("No salary outliers found.")
    else:
        print(salary_outliers)

    print_heading("OUTLIER TREATMENT")

    cleaned_df = cap_salary_outliers(cleaned_df)

    print("✓ Salary outliers capped successfully.")

    # ==========================================================
    # STEP 10 : FINAL VERIFICATION
    # ==========================================================

    print_heading("VERIFY MISSING VALUES")
    missing_value_report(cleaned_df)

    print_heading("VERIFY DUPLICATES")
    print(duplicate_summary(cleaned_df))

    # ==========================================================
    # STEP 11 : FINAL DATASET SHAPE
    # ==========================================================

    print_heading("FINAL DATASET SHAPE")
    dataset_shape(cleaned_df)

    # ==========================================================
    # STEP 12 : SAVE CLEANED DATASET
    # ==========================================================

    cleaned_df.to_csv(PROCESSED_DATA, index=False)

    print_heading("DATA SAVED")
    print(f"Cleaned dataset saved to:\n{PROCESSED_DATA}")

    # ==========================================================
    # STEP 13 : GENERATE REPORTS
    # ==========================================================

    print_heading("GENERATING REPORTS")

    write_summary_report(
        cleaned_df,
        SUMMARY_REPORT,
    )

    write_statistics_report(
        cleaned_df,
        STATISTICS_REPORT,
    )

    write_cleaning_report(
        original_rows=len(df),
        final_rows=len(cleaned_df),
        output_file=SUMMARY_REPORT.parent / "cleaning_report.txt",
    )

    print("✓ Summary Report Generated")
    print("✓ Statistics Report Generated")
    print("✓ Cleaning Report Generated")

    # ==========================================================
    # STEP 14 : GENERATE VISUALIZATIONS
    # ==========================================================

    print_heading("GENERATING VISUALIZATIONS")

    salary_distribution(
        cleaned_df,
        CHART_DIR / "salary_distribution.png",
    )

    department_count(
        cleaned_df,
        CHART_DIR / "department_count.png",
    )

    age_distribution(
        cleaned_df,
        CHART_DIR / "age_distribution.png",
    )

    performance_distribution(
        cleaned_df,
        CHART_DIR / "performance_distribution.png",
    )

    salary_boxplot(
        cleaned_df,
        CHART_DIR / "salary_boxplot.png",
    )

    correlation_heatmap(
        cleaned_df,
        CHART_DIR / "correlation_heatmap.png",
    )

    print("✓ All charts generated successfully.")

    # ==========================================================
    # STEP 15 : CLEANING SUMMARY
    # ==========================================================

    cleaning_summary(
        original_rows=len(df),
        final_rows=len(cleaned_df),
    )

    print_heading("PROCESS COMPLETED")

    print("🎉 Day 03 Professional Data Cleaning Completed Successfully!")


if __name__ == "__main__":
    main()