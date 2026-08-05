# 💼 Day 05 - NumPy Interview Questions

Author  : Purv Kevadiya  
Project : #100DaysOfDataScience  
Day     : 05

---

# Beginner Level

## 1. What is NumPy?

NumPy (Numerical Python) is an open-source Python library used for numerical computing. It provides the powerful `ndarray` object and numerous mathematical functions.

---

## 2. Why is NumPy faster than Python lists?

NumPy arrays:
- Store homogeneous data
- Use contiguous memory
- Are implemented in optimized C code
- Support vectorized operations

---

## 3. What is an ndarray?

`ndarray` is NumPy's N-dimensional array object used to efficiently store and manipulate numerical data.

---

## 4. How do you import NumPy?

```python
import numpy as np
```

---

## 5. How do you create a NumPy array?

```python
arr = np.array([1, 2, 3])
```

---

## 6. Difference between List and ndarray?

| Python List | NumPy Array |
|-------------|-------------|
| Slower | Faster |
| More memory | Less memory |
| Mixed data types | Same data type |
| Limited math operations | Optimized mathematical operations |

---

## 7. What does `shape` return?

The number of rows and columns (dimensions) of an array.

Example:

```python
arr.shape
```

---

## 8. What is `ndim`?

Returns the number of dimensions.

```python
arr.ndim
```

---

## 9. What is `size`?

Returns the total number of elements.

```python
arr.size
```

---

## 10. What is `dtype`?

Returns the data type of array elements.

```python
arr.dtype
```

---

# Array Creation

## 11. How do you create an array of zeros?

```python
np.zeros((3,3))
```

---

## 12. How do you create an array of ones?

```python
np.ones((2,4))
```

---

## 13. How do you create an identity matrix?

```python
np.eye(4)
```

---

## 14. Difference between `arange()` and `linspace()`?

**`arange()`** creates values using a step size.

```python
np.arange(0,10,2)
```

**`linspace()`** creates a specified number of evenly spaced values.

```python
np.linspace(0,10,5)
```

---

## 15. How do you generate random numbers?

```python
np.random.rand(3,3)
```

---

# Indexing & Slicing

## 16. How do you access the first element?

```python
arr[0]
```

---

## 17. How do you access the last element?

```python
arr[-1]
```

---

## 18. How do you slice an array?

```python
arr[2:6]
```

---

## 19. How do you access an element in a 2D array?

```python
arr[1,2]
```

---

## 20. What is negative indexing?

Negative indexing accesses elements from the end of the array.

---

# Reshaping

## 21. What does `reshape()` do?

Changes the shape of an array without changing its data.

```python
arr.reshape(3,3)
```

---

## 22. What is transpose?

Rows become columns and columns become rows.

```python
arr.T
```

---

## 23. Difference between `reshape()` and `transpose()`?

- `reshape()` changes dimensions.
- `transpose()` swaps axes.

---

# Statistics

## 24. Calculate mean.

```python
np.mean(arr)
```

---

## 25. Calculate median.

```python
np.median(arr)
```

---

## 26. Find minimum.

```python
np.min(arr)
```

---

## 27. Find maximum.

```python
np.max(arr)
```

---

## 28. Calculate standard deviation.

```python
np.std(arr)
```

---

## 29. Calculate variance.

```python
np.var(arr)
```

---

## 30. Calculate sum.

```python
np.sum(arr)
```

---

# Sorting

## 31. How do you sort an array?

```python
np.sort(arr)
```

---

## 32. Does `np.sort()` modify the original array?

No. It returns a sorted copy.

---

# Saving Arrays

## 33. How do you save a NumPy array?

```python
np.save("array.npy", arr)
```

---

## 34. How do you load a saved array?

```python
np.load("array.npy")
```

---

# Performance

## 35. What is vectorization?

Performing operations on entire arrays without explicit Python loops.

---

## 36. Why is vectorization important?

- Faster execution
- Cleaner code
- Better memory efficiency

---

# Applications

## 37. Where is NumPy used?

- Data Science
- Machine Learning
- Artificial Intelligence
- Deep Learning
- Computer Vision
- Finance
- Scientific Computing

---

## 38. Which libraries depend on NumPy?

- Pandas
- Matplotlib
- SciPy
- Scikit-learn
- TensorFlow
- PyTorch

---

# Coding Questions

## 39. Create an array from 1 to 10.

```python
np.arange(1,11)
```

---

## 40. Create a 3×3 identity matrix.

```python
np.eye(3)
```

---

## 41. Find the largest value in an array.

```python
np.max(arr)
```

---

## 42. Find the smallest value.

```python
np.min(arr)
```

---

## 43. Find the average.

```python
np.mean(arr)
```

---

## 44. Reshape a 1D array into a 3×3 matrix.

```python
arr.reshape(3,3)
```

---

## 45. Sort an array.

```python
np.sort(arr)
```

---

## 46. Find the number of dimensions.

```python
arr.ndim
```

---

## 47. Find the shape of an array.

```python
arr.shape
```

---

## 48. Find total elements.

```python
arr.size
```

---

## 49. Save and reload an array.

```python
np.save("sample.npy", arr)

loaded = np.load("sample.npy")
```

---

## 50. Why should every Data Scientist learn NumPy?

Because NumPy is the foundation of numerical computing in Python. Most data science, machine learning, and deep learning libraries are built on top of NumPy, making it an essential skill for efficient data manipulation and analysis.

---

# Revision Tips

- Understand `ndarray`
- Practice array creation
- Learn indexing and slicing
- Master reshaping
- Remember statistical functions
- Know when to use `arange()` vs `linspace()`
- Practice saving and loading arrays
- Focus on vectorization and performance

---

# Next Topic

Day 06 – Advanced NumPy & Matrix Operations

- Matrix Algebra
- Broadcasting
- Advanced Indexing
- Linear Algebra
- Performance Optimization