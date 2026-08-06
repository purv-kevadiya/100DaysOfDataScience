"""
Day 06 - Advanced NumPy

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 06

Professional demonstration of Advanced NumPy
operations including broadcasting, fancy indexing,
matrix operations, linear algebra and performance
comparison.
"""

import numpy as np

from config import (
    ARRAY_REPORT,
    PERFORMANCE_REPORT,
    SUMMARY_REPORT,
)

from helper import (
    print_heading,
    display_array,
    array_information,
    success,
)

from advanced_numpy import (
    create_copy,
    create_view,
    broadcast_add,
    broadcast_multiply,
    fancy_index,
    filter_greater_than,
    filter_between,
    create_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose_matrix,
    inverse_matrix,
    determinant,
    dot_product,
    cross_product,
    eigen_values,
    eigen_vectors,
    compare_execution_time,
)

from report import (
    write_summary_report,
    write_array_report,
    write_performance_report,
)


def main() -> None:
    """
    Execute complete Advanced NumPy workflow.
    """

    print_heading("DAY 06 - ADVANCED NUMPY")

    # ======================================================
    # CREATE SAMPLE ARRAY
    # ======================================================

    array = np.array([10, 20, 30, 40, 50])

    display_array("ORIGINAL ARRAY", array)

    array_information(array)

    # ======================================================
    # COPY vs VIEW
    # ======================================================

    print_heading("COPY VS VIEW")

    copied = create_copy(array)

    viewed = create_view(array)

    print("Copy :", copied)

    print("View :", viewed)

    # ======================================================
    # BROADCASTING
    # ======================================================

    print_heading("BROADCASTING")

    print("Add 10")

    print(broadcast_add(array, 10))

    print()

    print("Multiply by 2")

    print(broadcast_multiply(array, 2))

    # ======================================================
    # FANCY INDEXING
    # ======================================================

    print_heading("FANCY INDEXING")

    print(
        fancy_index(
            array,
            [0, 2, 4],
        )
    )

    # ======================================================
    # BOOLEAN MASKING
    # ======================================================

    print_heading("BOOLEAN MASKING")

    print("Greater than 25")

    print(
        filter_greater_than(
            array,
            25,
        )
    )

    print()

    print("Between 15 and 45")

    print(
        filter_between(
            array,
            15,
            45,
        )
    )

    # ======================================================
    # MATRIX OPERATIONS
    # ======================================================

    print_heading("MATRIX OPERATIONS")

    matrix1 = create_matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )

    matrix2 = create_matrix(
        [
            [5, 6],
            [7, 8],
        ]
    )

    print("Matrix A")

    print(matrix1)

    print()

    print("Matrix B")

    print(matrix2)

    print()

    print("Addition")

    print(add_matrices(matrix1, matrix2))

    print()

    print("Subtraction")

    print(subtract_matrices(matrix2, matrix1))

    print()

    print("Multiplication")

    print(multiply_matrices(matrix1, matrix2))

    print()

    print("Transpose")

    print(transpose_matrix(matrix1))

    print()

    print("Inverse")

    print(inverse_matrix(matrix1))

    print()

    print("Determinant")

    print(determinant(matrix1))

    # ======================================================
    # LINEAR ALGEBRA
    # ======================================================

    print_heading("LINEAR ALGEBRA")

    vector1 = np.array([1, 2, 3])

    vector2 = np.array([4, 5, 6])

    print("Dot Product")

    print(dot_product(vector1, vector2))

    print()

    print("Cross Product")

    print(cross_product(vector1, vector2))

    print()

    print("Eigen Values")

    print(eigen_values(matrix1))

    print()

    print("Eigen Vectors")

    print(eigen_vectors(matrix1))

    # ======================================================
    # PERFORMANCE
    # ======================================================

    print_heading("PERFORMANCE COMPARISON")

    large_array = np.arange(1_000_000)

    performance = compare_execution_time(
        large_array
    )

    for key, value in performance.items():

        print(f"{key:<20}: {value:.8f} sec")

    # ======================================================
    # REPORTS
    # ======================================================

    print_heading("GENERATING REPORTS")

    write_summary_report(
        SUMMARY_REPORT,
    )

    write_array_report(
        array,
        ARRAY_REPORT,
    )

    write_performance_report(
        performance,
        PERFORMANCE_REPORT,
    )

    success("Summary Report Generated")

    success("Array Report Generated")

    success("Performance Report Generated")

    # ======================================================
    # COMPLETED
    # ======================================================

    print_heading("PROCESS COMPLETED")

    print("🎉 Day 06 Advanced NumPy Completed Successfully!")


if __name__ == "__main__":
    main()