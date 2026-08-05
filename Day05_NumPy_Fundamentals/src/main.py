"""
Day 05 - NumPy Fundamentals

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 05

Professional demonstration of NumPy fundamentals.
"""

from config import (
    RAW_DATA,
    ARRAY_DIR,
    SUMMARY_REPORT,
    STATISTICS_REPORT,
    OPERATIONS_REPORT,
)

from helper import (
    print_heading,
    print_array_info,
    save_array,
)

from numpy_operations import (
    load_dataset,
    dataframe_to_numpy,
    create_array,
    create_zeros,
    create_ones,
    create_identity,
    create_arange,
    create_linspace,
    create_random_array,
    create_random_integer_array,
    first_element,
    last_element,
    reshape_array,
    transpose_array,
    mean,
    median,
    minimum,
    maximum,
    standard_deviation,
    variance,
    total,
    sort_array,
)

from report import (
    write_summary_report,
    write_statistics_report,
    write_operations_report,
)


def main() -> None:
    """
    Execute complete NumPy workflow.
    """

    # ==========================================================
    # STEP 1 : LOAD DATASET
    # ==========================================================

    print_heading("DAY 05 - NUMPY FUNDAMENTALS")

    df = load_dataset(RAW_DATA)

    print("✓ Dataset loaded successfully.")

    # ==========================================================
    # STEP 2 : CONVERT TO NUMPY
    # ==========================================================

    print_heading("CONVERT DATAFRAME TO NUMPY")

    data = dataframe_to_numpy(df)

    print_array_info(data, "Dataset Array")

    # ==========================================================
    # STEP 3 : ARRAY CREATION
    # ==========================================================

    print_heading("ARRAY CREATION")

    sample_array = create_array([10, 20, 30, 40, 50])

    print(sample_array)

    zeros = create_zeros((3, 3))
    ones = create_ones((3, 3))
    identity = create_identity(4)
    arange = create_arange(1, 11)
    linspace = create_linspace(0, 100, 11)
    random_array = create_random_array(3, 3)
    random_int = create_random_integer_array(
        1,
        100,
        (3, 3),
    )

    print("✓ Arrays created successfully.")

    # ==========================================================
    # STEP 4 : INDEXING
    # ==========================================================

    print_heading("INDEXING")

    print("First Element :", first_element(sample_array))
    print("Last Element  :", last_element(sample_array))

    # ==========================================================
    # STEP 5 : RESHAPING
    # ==========================================================

    print_heading("RESHAPING")

    reshaped = reshape_array(
        create_arange(1, 10),
        3,
        3,
    )

    print(reshaped)

    print("\nTranspose\n")

    print(transpose_array(reshaped))

    # ==========================================================
    # STEP 6 : STATISTICS
    # ==========================================================

    print_heading("STATISTICS")

    print(f"Mean     : {mean(sample_array)}")
    print(f"Median   : {median(sample_array)}")
    print(f"Minimum  : {minimum(sample_array)}")
    print(f"Maximum  : {maximum(sample_array)}")
    print(f"Std Dev  : {standard_deviation(sample_array)}")
    print(f"Variance : {variance(sample_array)}")
    print(f"Total    : {total(sample_array)}")

    # ==========================================================
    # STEP 7 : SORTING
    # ==========================================================

    print_heading("SORTING")

    unsorted = create_array(
        [45, 12, 67, 4, 88, 21]
    )

    print("Original :", unsorted)

    print("Sorted   :", sort_array(unsorted))

    # ==========================================================
    # STEP 8 : SAVE ARRAYS
    # ==========================================================

    print_heading("SAVING ARRAYS")

    save_array(
        sample_array,
        ARRAY_DIR / "sample_array.npy",
    )

    save_array(
        reshaped,
        ARRAY_DIR / "reshaped_array.npy",
    )

    print("✓ Arrays saved successfully.")

    # ==========================================================
    # STEP 9 : GENERATE REPORTS
    # ==========================================================

    print_heading("GENERATING REPORTS")

    write_summary_report(
        sample_array,
        SUMMARY_REPORT,
    )

    write_statistics_report(
        sample_array,
        STATISTICS_REPORT,
    )

    write_operations_report(
        sample_array,
        OPERATIONS_REPORT,
    )

    print("✓ Summary Report Generated")
    print("✓ Statistics Report Generated")
    print("✓ Operations Report Generated")

    # ==========================================================
    # COMPLETED
    # ==========================================================

    print_heading("PROCESS COMPLETED")

    print("🎉 Day 05 NumPy Fundamentals Completed Successfully!")


if __name__ == "__main__":
    main()