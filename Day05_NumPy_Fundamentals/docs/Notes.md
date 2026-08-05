# 📘 Day 05 - NumPy Fundamentals Notes

Author  : Purv Kevadiya  
Project : #100DaysOfDataScience  
Day     : 05

---

# What is NumPy?

NumPy (Numerical Python) is the fundamental Python library used for numerical computing. It provides a powerful multidimensional array object (`ndarray`) along with a collection of mathematical functions for performing fast operations on arrays.

NumPy is significantly faster than native Python lists because it stores homogeneous data in contiguous memory and performs operations using optimized C implementations.

---

# Why Use NumPy?

NumPy offers several advantages:

- Faster execution than Python lists
- Less memory consumption
- Efficient mathematical operations
- Vectorized computation
- Supports multidimensional arrays
- Foundation for Pandas, SciPy, Scikit-learn, TensorFlow, and PyTorch

---

# Installing NumPy

```bash
pip install numpy
```

Import NumPy:

```python
import numpy as np
```

---

# NumPy Array (ndarray)

The primary data structure in NumPy is the `ndarray`.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
```

Output:

```text
[10 20 30 40]
```

---

# Creating Arrays

## One-Dimensional Array

```python
arr = np.array([1, 2, 3])
```

---

## Two-Dimensional Array

```python
arr = np.array([
    [1, 2],
    [3, 4]
])
```

---

## Zeros Array

```python
np.zeros((3, 3))
```

---

## Ones Array

```python
np.ones((2, 4))
```

---

## Identity Matrix

```python
np.eye(4)
```

---

## Range of Numbers

```python
np.arange(1, 11)
```

---

## Evenly Spaced Values

```python
np.linspace(0, 100, 5)
```

---

## Random Numbers

```python
np.random.rand(3, 3)
```

---

# Array Properties

```python
arr.shape
arr.ndim
arr.size
arr.dtype
arr.itemsize
arr.nbytes
```

Example:

```text
Shape      : (3, 4)
Dimensions : 2
Size       : 12
Data Type  : int64
```

---

# Indexing

```python
arr[0]

arr[-1]
```

For 2D arrays:

```python
arr[1][2]

arr[1,2]
```

---

# Slicing

```python
arr[2:8]

arr[:5]

arr[5:]
```

2D slicing:

```python
arr[0:2,1:3]
```

---

# Reshaping Arrays

```python
arr.reshape(3,3)
```

Original:

```text
1 2 3 4 5 6 7 8 9
```

Reshaped:

```text
1 2 3
4 5 6
7 8 9
```

---

# Transpose

```python
matrix.T
```

Example:

```text
1 2
3 4
```

Becomes

```text
1 3
2 4
```

---

# Statistical Functions

Mean

```python
np.mean(arr)
```

Median

```python
np.median(arr)
```

Minimum

```python
np.min(arr)
```

Maximum

```python
np.max(arr)
```

Standard Deviation

```python
np.std(arr)
```

Variance

```python
np.var(arr)
```

Sum

```python
np.sum(arr)
```

---

# Sorting

```python
np.sort(arr)
```

Example

Before

```text
45 12 67 4
```

After

```text
4 12 45 67
```

---

# Saving Arrays

```python
np.save("array.npy", arr)
```

Load

```python
np.load("array.npy")
```

---

# Advantages of NumPy

- Fast execution
- Memory efficient
- Powerful mathematical functions
- Vectorized operations
- Supports multidimensional arrays
- Easy integration with Data Science libraries

---

# Real-World Applications

- Data Science
- Machine Learning
- Artificial Intelligence
- Computer Vision
- Image Processing
- Financial Analysis
- Scientific Computing
- Deep Learning
- Statistics
- Big Data

---

# Key Takeaways

- NumPy is the foundation of the Python Data Science ecosystem.
- `ndarray` is much faster than Python lists.
- NumPy simplifies mathematical computations.
- Reshaping and indexing are essential skills.
- Statistical functions are built in and highly optimized.
- Learning NumPy is the first step toward mastering Machine Learning and AI.

---

# Next Topic

Day 06 – Advanced NumPy & Matrix Operations

- Matrix Algebra
- Broadcasting
- Vectorization
- Linear Algebra
- Performance Optimization