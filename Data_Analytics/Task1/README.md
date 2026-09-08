# Task 1 - Data Cleaning & Preprocessing

**Internship:** Data Analytics Virtual Internship
**Organization:** CodSoft
**Intern Name:** Suman D H
**Internship ID:** BY26RY233444
**Internship Duration:** 25 August 2026 to 25 September 2026
**Date:** 25/08/2026

## Objective
Import a dataset, inspect its structure, identify data quality issues
(missing values, duplicates, inconsistent entries), clean the dataset, and
prepare it for further analysis using Pandas.

## Files in this folder
| File | Description |
|---|---|
| `customer_data_raw.csv` | Raw synthetic customer dataset with intentional missing values, duplicate rows, and inconsistent formatting (used as the task input). |
| `generate_raw_dataset.py` | Script used to generate the raw dataset (for reproducibility). |
| `source_code.py` | Main task script: inspects, cleans, and exports the dataset. |
| `customer_data_cleaned.csv` | Output: cleaned dataset (bonus deliverable). |
| `output.png` | Output: bar chart comparing missing values before vs. after cleaning. |
| `requirements.txt` | Python dependencies required to run the script. |

## What the script does
1. Loads `customer_data_raw.csv` and inspects shape, dtypes, and sample rows.
2. Identifies missing values, duplicate rows, and inconsistent text entries
   (e.g. mixed-case Gender/City values, Age stored as text in some rows).
3. Cleans the data:
   - Removes duplicate rows
   - Converts `Age` to numeric and fills missing values with the median
   - Standardizes `Gender` and `City` text casing
   - Fills missing `PurchaseAmount`/`Rating`/`City` values
   - Converts `SignupDate` to a proper datetime type
4. Saves the cleaned dataset to `customer_data_cleaned.csv`.
5. Generates a before/after missing-values comparison chart (`output.png`).

## How to run
```bash
pip install -r requirements.txt
python source_code.py
```

## Output Preview
See `output.png` for the missing-values comparison chart.

---
*Submitted as part of the CodSoft Data Analytics Internship.*
