"""
NumPy Operations Module

Author  : Purv Kevadiya
Project : #100DaysOfDataScience
Day     : 05

Reusable NumPy functions for array creation,
inspection and manipulation.
"""

import numpy as np
import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load CSV dataset.

    Args:
        file_path: CSV file path.

    Returns:
        Pandas DataFrame.
    """

    return pd.read_csv(file_path)


def dataframe_to_numpy(
    df: pd.DataFrame,
) -> np.ndarray:
    """
    Convert DataFrame to NumPy array.

    Args:
        df: Input DataFrame.

    Returns:
        NumPy ndarray.
    """

    return df.to_numpy()

# ==========================================================
# ARRAY CREATION
# ==========================================================

def create_array(data: list) -> np.ndarray:
    """
    Create NumPy array from list.
    """

    return np.array(data)


def create_zeros(shape: tuple) -> np.ndarray:
    """
    Create zero array.
    """

    return np.zeros(shape)


def create_ones(shape: tuple) -> np.ndarray:
    """
    Create ones array.
    """

    return np.ones(shape)


def create_full(
    shape: tuple,
    value: int,
) -> np.ndarray:
    """
    Create filled array.
    """

    return np.full(shape, value)


def create_identity(size: int) -> np.ndarray:
    """
    Create identity matrix.
    """

    return np.eye(size)


def create_arange(
    start: int,
    stop: int,
    step: int = 1,
) -> np.ndarray:
    """
    Create arange array.
    """

    return np.arange(start, stop, step)


def create_linspace(
    start: int,
    stop: int,
    num: int,
) -> np.ndarray:
    """
    Create linspace array.
    """

    return np.linspace(start, stop, num)

# ==========================================================
# RANDOM ARRAYS
# ==========================================================

def create_random_array(
    rows: int,
    columns: int,
) -> np.ndarray:
    """
    Create random array.
    """

    np.random.seed(42)

    return np.random.rand(rows, columns)


def create_random_integer_array(
    low: int,
    high: int,
    size: tuple,
) -> np.ndarray:
    """
    Create random integer array.
    """

    np.random.seed(42)

    return np.random.randint(
        low,
        high,
        size=size,
    )

# ==========================================================
# ARRAY PROPERTIES
# ==========================================================

def array_shape(array: np.ndarray):
    """
    Return array shape.
    """

    return array.shape


def array_size(array: np.ndarray):
    """
    Return array size.
    """

    return array.size


def array_dimension(array: np.ndarray):
    """
    Return number of dimensions.
    """

    return array.ndim


def array_dtype(array: np.ndarray):
    """
    Return array datatype.
    """

    return array.dtype


def array_itemsize(array: np.ndarray):
    """
    Return item size.
    """

    return array.itemsize


def array_memory(array: np.ndarray):
    """
    Return memory usage.
    """

    return array.nbytes

# ==========================================================
# INDEXING
# ==========================================================

def first_element(array: np.ndarray):
    """
    Return first element.
    """

    return array[0]


def last_element(array: np.ndarray):
    """
    Return last element.
    """

    return array[-1]


def element_at(
    array: np.ndarray,
    index: int,
):
    """
    Return element at given index.
    """

    return array[index]


def row_at(
    array: np.ndarray,
    index: int,
) -> np.ndarray:
    """
    Return row from 2D array.
    """

    return array[index]


def column_at(
    array: np.ndarray,
    index: int,
) -> np.ndarray:
    """
    Return column from 2D array.
    """

    return array[:, index]


def element_2d(
    array: np.ndarray,
    row: int,
    column: int,
):
    """
    Return single element from 2D array.
    """

    return array[row, column]

# ==========================================================
# ARRAY SLICING
# ==========================================================

def slice_array(
    array: np.ndarray,
    start: int,
    stop: int,
) -> np.ndarray:
    """
    Slice 1D array.
    """

    return array[start:stop]


def slice_with_step(
    array: np.ndarray,
    start: int,
    stop: int,
    step: int,
) -> np.ndarray:
    """
    Slice array using step.
    """

    return array[start:stop:step]


def reverse_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Reverse array.
    """

    return array[::-1]


def slice_rows(
    array: np.ndarray,
    start: int,
    stop: int,
) -> np.ndarray:
    """
    Slice rows.
    """

    return array[start:stop]


def slice_columns(
    array: np.ndarray,
    start: int,
    stop: int,
) -> np.ndarray:
    """
    Slice columns.
    """

    return array[:, start:stop]

# ==========================================================
# RESHAPING
# ==========================================================

def reshape_array(
    array: np.ndarray,
    rows: int,
    columns: int,
) -> np.ndarray:
    """
    Reshape array.
    """

    return array.reshape(rows, columns)


def flatten_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Flatten array.
    """

    return array.flatten()


def ravel_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Return flattened view.
    """

    return array.ravel()


def transpose_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Transpose array.
    """

    return array.T

# ==========================================================
# MATHEMATICAL OPERATIONS
# ==========================================================

def add_arrays(
    array1: np.ndarray,
    array2: np.ndarray,
) -> np.ndarray:
    """
    Add arrays.
    """

    return np.add(array1, array2)


def subtract_arrays(
    array1: np.ndarray,
    array2: np.ndarray,
) -> np.ndarray:
    """
    Subtract arrays.
    """

    return np.subtract(array1, array2)


def multiply_arrays(
    array1: np.ndarray,
    array2: np.ndarray,
) -> np.ndarray:
    """
    Multiply arrays.
    """

    return np.multiply(array1, array2)


def divide_arrays(
    array1: np.ndarray,
    array2: np.ndarray,
) -> np.ndarray:
    """
    Divide arrays.
    """

    return np.divide(array1, array2)


def square_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Square each element.
    """

    return np.square(array)


def sqrt_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Square root.
    """

    return np.sqrt(array)

# ==========================================================
# STATISTICS
# ==========================================================

def mean(array: np.ndarray):
    """
    Return mean.
    """

    return np.mean(array)


def median(array: np.ndarray):
    """
    Return median.
    """

    return np.median(array)


def minimum(array: np.ndarray):
    """
    Return minimum value.
    """

    return np.min(array)


def maximum(array: np.ndarray):
    """
    Return maximum value.
    """

    return np.max(array)


def standard_deviation(array: np.ndarray):
    """
    Return standard deviation.
    """

    return np.std(array)


def variance(array: np.ndarray):
    """
    Return variance.
    """

    return np.var(array)


def total(array: np.ndarray):
    """
    Return total.
    """

    return np.sum(array)

# ==========================================================
# SORTING
# ==========================================================

def sort_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Sort array.
    """

    return np.sort(array)


def argsort_array(
    array: np.ndarray,
) -> np.ndarray:
    """
    Return sorting indices.
    """

    return np.argsort(array)


# ==========================================================
# FILTERING
# ==========================================================

def filter_greater_than(
    array: np.ndarray,
    value: float,
) -> np.ndarray:
    """
    Return values greater than given value.
    """

    return array[array > value]


def filter_less_than(
    array: np.ndarray,
    value: float,
) -> np.ndarray:
    """
    Return values less than given value.
    """

    return array[array < value]


def filter_equal(
    array: np.ndarray,
    value,
) -> np.ndarray:
    """
    Return values equal to given value.
    """

    return array[array == value]