"""
Task 1: Data Cleaning & Preprocessing
CodSoft Data Analytics Internship
Author: Suman D H

Steps performed:
1. Import dataset and inspect structure
2. Identify missing values, duplicates, inconsistent entries
3. Clean the dataset (handle nulls, remove duplicates, fix dtypes)
4. Prepare data for further analysis
5. Bonus: Save cleaned dataset as new CSV
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# 1. Import dataset and inspect structure
# ----------------------------------------------------------------
df = pd.read_csv("customer_data_raw.csv")

print("Shape of raw dataset:", df.shape)
print("\nColumn info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# ----------------------------------------------------------------
# 2. Identify missing values, duplicates, inconsistent entries
# ----------------------------------------------------------------
missing_before = df.isnull().sum()
duplicate_count = df.duplicated().sum()
print("\nMissing values per column (before cleaning):\n", missing_before)
print("\nNumber of duplicate rows:", duplicate_count)
print("\nUnique values in 'Gender' (inconsistent casing):", df["Gender"].unique())
print("Unique values in 'City' (inconsistent casing):", df["City"].unique())

# ----------------------------------------------------------------
# 3. Clean the dataset
# ----------------------------------------------------------------
df_clean = df.copy()

# Remove exact duplicate rows
df_clean = df_clean.drop_duplicates()

# Fix inconsistent dtypes: Age should be numeric
df_clean["Age"] = pd.to_numeric(df_clean["Age"], errors="coerce")

# Standardize categorical text (Gender, City)
df_clean["Gender"] = df_clean["Gender"].str.strip().str.upper().replace({
    "MALE": "Male", "M": "Male", "FEMALE": "Female", "F": "Female"
})
df_clean["City"] = df_clean["City"].str.strip().str.title()

# Handle missing values
df_clean["Age"] = df_clean["Age"].fillna(df_clean["Age"].median())
df_clean["PurchaseAmount"] = df_clean["PurchaseAmount"].fillna(df_clean["PurchaseAmount"].median())
df_clean["Rating"] = df_clean["Rating"].fillna(df_clean["Rating"].mode()[0])
df_clean["City"] = df_clean["City"].fillna("Unknown")

# Correct data types
df_clean["Age"] = df_clean["Age"].astype(int)
df_clean["Rating"] = df_clean["Rating"].astype(int)
df_clean["SignupDate"] = pd.to_datetime(df_clean["SignupDate"])

missing_after = df_clean.isnull().sum()

# ----------------------------------------------------------------
# 4. Visual summary of cleaning results (output image)
# ----------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

missing_before.plot(kind="bar", ax=axes[0], color="salmon")
axes[0].set_title("Missing Values BEFORE Cleaning")
axes[0].set_ylabel("Count")
axes[0].tick_params(axis='x', rotation=45)

missing_after.plot(kind="bar", ax=axes[1], color="seagreen")
axes[1].set_title("Missing Values AFTER Cleaning")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis='x', rotation=45)

plt.suptitle("Task 1: Data Cleaning Summary - Missing Values Before vs After")
plt.tight_layout()
plt.savefig("output.png", dpi=150)
plt.close()

# ----------------------------------------------------------------
# 5. Bonus: Save cleaned dataset as new CSV
# ----------------------------------------------------------------
df_clean.to_csv("customer_data_cleaned.csv", index=False)

print("\nShape after cleaning:", df_clean.shape)
print("Missing values after cleaning:\n", missing_after)
print("\nCleaned dataset saved as 'customer_data_cleaned.csv'")
print("Summary chart saved as 'output.png'")
