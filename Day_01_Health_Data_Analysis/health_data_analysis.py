import pandas as pd
import numpy as np
from pathlib import Path

# -----------------------------
# Create a DataFrame
# -----------------------------

d = {
    "col1": [1, 2, 3, 4, 7],
    "col2": [4, 5, 6, 9, 5],
    "col3": [7, 8, 12, 1, 11]
}

df = pd.DataFrame(d)

print("DataFrame:")
print(df)

# -----------------------------
# Basic Statistics
# -----------------------------

average_pulse = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]

print("\nMaximum Average Pulse:", max(average_pulse))
print("Minimum Average Pulse:", min(average_pulse))

calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

print("Average Calorie Burnage:", np.mean(calorie_burnage))

# -----------------------------
# Read CSV File
# -----------------------------

csv_file = Path(__file__).parent / "health_data.csv"

health_data = pd.read_csv(csv_file)

print("\nComplete Dataset:")
print(health_data)

print("\nFirst Five Rows:")
print(health_data.head())

# -----------------------------
# Data Cleaning
# -----------------------------

health_data.dropna(inplace=True)

print("\nDataset Information:")
print(health_data.info())

# -----------------------------
# Change Data Types
# -----------------------------

health_data["Average_Pulse"] = health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print("\nUpdated Dataset Information:")
print(health_data.info())

# -----------------------------
# Data Analysis
# -----------------------------

pd.set_option("display.max_columns", None)

print("\nStatistical Summary:")
print(health_data.describe())