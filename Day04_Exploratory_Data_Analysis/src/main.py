"""
Day 04 - Professional Data Visualization

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 04

This module generates professional visualizations
using the cleaned dataset produced in Day 03.
"""

import config

from helper import (
    print_heading,
)

from visualization import (
    load_dataset,
    plot_salary_line_chart,
    plot_department_count,
    plot_age_distribution,
    plot_experience_vs_salary,
    plot_performance_distribution,
    plot_salary_boxplot,
    plot_correlation_heatmap,
    plot_dashboard,
)


def main() -> None:
    """
    Execute complete visualization workflow.
    """

    # ==========================================================
    # LOAD DATASET
    # ==========================================================

    print_heading("DAY 04 - PROFESSIONAL DATA VISUALIZATION")

    df = load_dataset(config.PROCESSED_DATA)

    print("✓ Cleaned dataset loaded successfully.")

    # ==========================================================
    # GENERATE VISUALIZATIONS
    # ==========================================================

    print_heading("GENERATING VISUALIZATIONS")

    plot_salary_line_chart(
        df,
        config.CHART_DIR / "salary_line_chart.png",
    )
    print("✓ Salary Line Chart")

    plot_department_count(
        df,
        config.CHART_DIR / "department_count.png",
    )
    print("✓ Department Count")

    plot_age_distribution(
        df,
        config.CHART_DIR / "age_distribution.png",
    )
    print("✓ Age Distribution")

    plot_experience_vs_salary(
        df,
        config.CHART_DIR / "experience_vs_salary.png",
    )
    print("✓ Experience vs Salary")

    plot_performance_distribution(
        df,
        config.CHART_DIR / "performance_distribution.png",
    )
    print("✓ Performance Distribution")

    plot_salary_boxplot(
        df,
        config.CHART_DIR / "salary_boxplot.png",
    )
    print("✓ Salary Box Plot")

    plot_correlation_heatmap(
        df,
        config.CHART_DIR / "correlation_heatmap.png",
    )
    print("✓ Correlation Heatmap")

    plot_dashboard(
        df,
        config.CHART_DIR / "dashboard.png",
    )
    print("✓ Dashboard")

    # ==========================================================
    # COMPLETED
    # ==========================================================

    print_heading("PROCESS COMPLETED")

    print("🎉 All visualizations generated successfully.")
    print(f"\nCharts saved to:\n{config.CHART_DIR}")


if __name__ == "__main__":
    main()