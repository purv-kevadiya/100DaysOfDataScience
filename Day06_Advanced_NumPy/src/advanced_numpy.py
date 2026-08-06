"""
Advanced NumPy Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 06

Reusable functions for Advanced NumPy,
Matrix Operations and Linear Algebra.
"""

import time

import numpy as np

# ==========================================================
# COPY vs VIEW
# ==========================================================

def create_copy(
    array: np.ndarray,
) -> np.ndarray:
    """
    Return deep copy of array.
    """

    return array.copy()


def create_view(
    array: np.ndarray,
) -> np.ndarray:
    """
    Return array view.
    """

    return array.view()

# ==========================================================
# BROADCASTING
# ==========================================================

def broadcast_add(
    array: np.ndarray,
    value: float,
) -> np.ndarray:
    """
    Add scalar using broadcasting.
    """

    return array + value


def broadcast_multiply(
    array: np.ndarray,
    value: float,
) -> np.ndarray:
    """
    Multiply scalar using broadcasting.
    """

    return array * value

# ==========================================================
# FANCY INDEXING
# ==========================================================

def fancy_index(
    array: np.ndarray,
    indices: list,
) -> np.ndarray:
    """
    Return elements using fancy indexing.
    """

    return array[indices]

# ==========================================================
# BOOLEAN MASKING
# ==========================================================

def filter_greater_than(
    array: np.ndarray,
    value: float,
) -> np.ndarray:
    """
    Filter values greater than threshold.
    """

    return array[array > value]


def filter_between(
    array: np.ndarray,
    minimum: float,
    maximum: float,
) -> np.ndarray:
    """
    Filter values between range.
    """

    return array[
        (array >= minimum)
        &
        (array <= maximum)
    ]

# ==========================================================
# MATRIX CREATION
# ==========================================================

def create_matrix(
    data: list,
) -> np.ndarray:
    """
    Create NumPy matrix from nested list.

    Args:
        data: Nested list.

    Returns:
        NumPy matrix.
    """

    return np.array(data)


# ==========================================================
# MATRIX ADDITION
# ==========================================================

def add_matrices(
    matrix1: np.ndarray,
    matrix2: np.ndarray,
) -> np.ndarray:
    """
    Add two matrices.
    """

    return np.add(
        matrix1,
        matrix2,
    )


# ==========================================================
# MATRIX SUBTRACTION
# ==========================================================

def subtract_matrices(
    matrix1: np.ndarray,
    matrix2: np.ndarray,
) -> np.ndarray:
    """
    Subtract two matrices.
    """

    return np.subtract(
        matrix1,
        matrix2,
    )


# ==========================================================
# MATRIX MULTIPLICATION
# ==========================================================

def multiply_matrices(
    matrix1: np.ndarray,
    matrix2: np.ndarray,
) -> np.ndarray:
    """
    Matrix multiplication.
    """

    return np.matmul(
        matrix1,
        matrix2,
    )


# ==========================================================
# MATRIX TRANSPOSE
# ==========================================================

def transpose_matrix(
    matrix: np.ndarray,
) -> np.ndarray:
    """
    Matrix transpose.
    """

    return matrix.T


# ==========================================================
# MATRIX INVERSE
# ==========================================================

def inverse_matrix(
    matrix: np.ndarray,
) -> np.ndarray:
    """
    Matrix inverse.
    """

    return np.linalg.inv(matrix)


# ==========================================================
# MATRIX DETERMINANT
# ==========================================================

def determinant(
    matrix: np.ndarray,
) -> float:
    """
    Matrix determinant.
    """

    return np.linalg.det(matrix)

# ==========================================================
# LINEAR ALGEBRA
# ==========================================================

def dot_product(
    vector1: np.ndarray,
    vector2: np.ndarray,
) -> float:
    """
    Compute dot product of two vectors.

    Args:
        vector1: First vector.
        vector2: Second vector.

    Returns:
        Dot product.
    """

    return np.dot(
        vector1,
        vector2,
    )


def cross_product(
    vector1: np.ndarray,
    vector2: np.ndarray,
) -> np.ndarray:
    """
    Compute cross product.

    Args:
        vector1: First vector.
        vector2: Second vector.

    Returns:
        Cross product.
    """

    return np.cross(
        vector1,
        vector2,
    )


def eigen_values(
    matrix: np.ndarray,
) -> np.ndarray:
    """
    Return eigen values.

    Args:
        matrix: Square matrix.

    Returns:
        Eigen values.
    """

    values, _ = np.linalg.eig(matrix)

    return values


def eigen_vectors(
    matrix: np.ndarray,
) -> np.ndarray:
    """
    Return eigen vectors.

    Args:
        matrix: Square matrix.

    Returns:
        Eigen vectors.
    """

    _, vectors = np.linalg.eig(matrix)

    return vectors


# ==========================================================
# VECTORIZATION
# ==========================================================

def square_using_loop(
    array: np.ndarray,
) -> np.ndarray:
    """
    Square values using Python loop.
    """

    result = []

    for value in array:
        result.append(value ** 2)

    return np.array(result)


def square_using_numpy(
    array: np.ndarray,
) -> np.ndarray:
    """
    Square values using NumPy vectorization.
    """

    return np.square(array)


# ==========================================================
# PERFORMANCE COMPARISON
# ==========================================================

def compare_execution_time(
    array: np.ndarray,
) -> dict:
    """
    Compare Python loop vs NumPy execution time.

    Args:
        array: Input array.

    Returns:
        Dictionary containing execution times.
    """

    start = time.perf_counter()

    square_using_loop(array)

    loop_time = time.perf_counter() - start

    start = time.perf_counter()

    square_using_numpy(array)

    numpy_time = time.perf_counter() - start

    return {
        "Loop Time": loop_time,
        "NumPy Time": numpy_time,
    }