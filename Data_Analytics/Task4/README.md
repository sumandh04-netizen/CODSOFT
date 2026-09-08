# Task 4 - Customer Data Analysis

**Internship:** Data Analytics Virtual Internship
**Organization:** CodSoft
**Intern Name:** Suman D H
**Internship ID:** BY26RY233444
**Internship Duration:** 25 August 2026 to 25 September 2026
**Date:** 25/08/2026

## Objective
Analyze customer information to understand purchasing behavior, segment
customers by age/location/buying patterns, identify the most valuable
customer groups, and create visual reports with marketing recommendations.

## Files in this folder
| File | Description |
|---|---|
| `customer_dataset.csv` | Input dataset (cleaned customer data). |
| `source_code.py` | Main customer analysis script. |
| `output.png` | Output: 4-panel visual report (segments, high-value customers). |
| `high_value_customers.csv` | Output: list of top 10% highest-spending customers. |
| `marketing_strategy.txt` | Bonus: marketing strategy suggestions based on the analysis. |
| `requirements.txt` | Python dependencies required to run the script. |

## What the script does
1. Summarizes overall purchasing behavior.
2. Segments customers into age groups (18-25, 26-35, 36-45, 46-55, 56-70)
   and by city, computing customer count, average purchase, and total revenue
   per segment.
3. Identifies the top 10% of customers by spend as "high-value customers"
   and exports them to `high_value_customers.csv`.
4. Builds a 4-panel visual report (`output.png`) showing segment counts,
   average purchase per age group, total revenue per city, and high-value
   customers highlighted on a scatter plot.
5. Generates data-driven marketing strategy suggestions
   (`marketing_strategy.txt`).

## How to run
```bash
pip install -r requirements.txt
python source_code.py
```

---
*Submitted as part of the CodSoft Data Analytics Internship.*
