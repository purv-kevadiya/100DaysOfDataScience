# 📊 Day 05 - Workflow

Author  : Purv Kevadiya  
Project : #100DaysOfDataScience  
Day     : 05

---

# Project Workflow

This document explains the complete workflow of the **Day 05 – NumPy Fundamentals** project.

The project is designed using a modular architecture where each module has a specific responsibility.

---

# Overall Workflow

```text
                START
                  │
                  ▼
         Load Employee Dataset
                  │
                  ▼
     Convert DataFrame to NumPy Array
                  │
                  ▼
        Display Array Properties
                  │
                  ▼
         Create Sample Arrays
                  │
                  ▼
      Perform Indexing Operations
                  │
                  ▼
      Perform Reshaping Operations
                  │
                  ▼
      Calculate Statistics
                  │
                  ▼
         Perform Sorting
                  │
                  ▼
         Save NumPy Arrays
                  │
                  ▼
      Generate Text Reports
                  │
                  ▼
          Display Summary
                  │
                  ▼
                 END
```

---

# Step 1 — Load Dataset

The cleaned employee dataset is loaded from the `data/processed` directory using Pandas.

```python
df = pd.read_csv(PROCESSED_DATA)
```

Purpose:

- Read CSV file
- Store data in a DataFrame
- Prepare for NumPy conversion

---

# Step 2 — Convert DataFrame to NumPy

The numerical columns are converted into a NumPy array.

```python
array = df.to_numpy()
```

Purpose:

- Convert structured tabular data into a NumPy ndarray
- Enable high-performance numerical operations

---

# Step 3 — Display Array Properties

Display important properties:

- Shape
- Dimensions
- Size
- Data Type
- Item Size
- Memory Usage

Example:

```text
Shape      : (10, 4)
Dimensions : 2
Size       : 40
Data Type  : int64
Memory     : 320 bytes
```

---

# Step 4 — Array Creation

Create different arrays using NumPy.

Examples:

```python
np.array()

np.zeros()

np.ones()

np.arange()

np.linspace()

np.eye()
```

Purpose:

- Learn different array creation techniques
- Understand ndarray initialization

---

# Step 5 — Indexing

Access elements using positive and negative indexing.

Example:

```python
array[0]

array[-1]
```

Purpose:

- Retrieve specific elements efficiently

---

# Step 6 — Reshaping

Change the shape of an array without changing the data.

Example:

```python
array.reshape(3, 3)
```

Also perform transpose operation.

Purpose:

- Prepare data for mathematical operations
- Understand matrix orientation

---

# Step 7 — Statistical Operations

Calculate common statistics.

Functions used:

- Mean
- Median
- Minimum
- Maximum
- Standard Deviation
- Variance
- Sum

Purpose:

- Perform quick numerical analysis
- Understand NumPy aggregation functions

---

# Step 8 — Sorting

Sort values in ascending order.

Example:

```python
np.sort(array)
```

Purpose:

- Organize numerical data
- Prepare data for analysis

---

# Step 9 — Save Arrays

Save NumPy arrays using `.npy` format.

```python
np.save()
```

Purpose:

- Store arrays efficiently
- Reload without conversion

---

# Step 10 — Generate Reports

Automatically create:

- Summary Report
- Statistics Report
- Operations Report

Purpose:

- Document project results
- Produce reusable outputs

---

# Project Architecture

```text
main.py
│
├── config.py
│
├── helper.py
│
├── numpy_operations.py
│
├── report.py
│
└── outputs/
```

Each module has a single responsibility, making the project easier to maintain and extend.

---

# Learning Outcomes

After completing this project, you will understand:

- NumPy arrays
- ndarray properties
- Array creation
- Indexing
- Reshaping
- Statistical analysis
- Sorting
- Saving arrays
- Modular Python development
- Professional project organization

---

# Next Step

Day 06 – Advanced NumPy & Matrix Operations

Topics include:

- Matrix Algebra
- Broadcasting
- Vectorization
- Linear Algebra
- Performance Optimization