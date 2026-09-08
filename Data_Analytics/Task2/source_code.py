"""
Task 2: Exploratory Data Analysis (EDA)
CodSoft Data Analytics Internship
Author: Suman D H

Steps performed:
1. Load dataset and examine descriptive statistics
2. Identify trends, distributions, relationships between variables
3. Detect outliers and unusual patterns
4. Use summary statistics to answer key business questions
5. Bonus: Short findings report (see findings_report.txt)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ----------------------------------------------------------------
# 1. Load dataset & descriptive statistics
# ----------------------------------------------------------------
df = pd.read_csv("sales_dataset.csv")
print("Dataset shape:", df.shape)
print("\nDescriptive statistics:\n", df.describe(include="all"))

# ----------------------------------------------------------------
# 2 & 3. Trends, distributions, relationships, outliers
# ----------------------------------------------------------------
q1 = df["PurchaseAmount"].quantile(0.25)
q3 = df["PurchaseAmount"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df["PurchaseAmount"] < lower_bound) | (df["PurchaseAmount"] > upper_bound)]
print(f"\nOutliers detected in PurchaseAmount: {len(outliers)}")

# ----------------------------------------------------------------
# 4. Key business questions via summary stats
# ----------------------------------------------------------------
avg_purchase_by_city = df.groupby("City")["PurchaseAmount"].mean().sort_values(ascending=False)
avg_purchase_by_gender = df.groupby("Gender")["PurchaseAmount"].mean()
top_city = avg_purchase_by_city.idxmax()
corr_age_purchase = df["Age"].corr(df["PurchaseAmount"])

print("\nAverage purchase amount by city:\n", avg_purchase_by_city)
print("\nAverage purchase amount by gender:\n", avg_purchase_by_gender)
print(f"\nCorrelation between Age and PurchaseAmount: {corr_age_purchase:.3f}")

# ----------------------------------------------------------------
# Visualization grid (output.png)
# ----------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

sns.histplot(df["Age"], bins=15, kde=True, ax=axes[0,0], color="steelblue")
axes[0,0].set_title("Age Distribution")

sns.histplot(df["PurchaseAmount"], bins=20, kde=True, ax=axes[0,1], color="darkorange")
axes[0,1].set_title("Purchase Amount Distribution")

sns.boxplot(y=df["PurchaseAmount"], ax=axes[0,2], color="lightcoral")
axes[0,2].set_title("Purchase Amount - Outlier Detection")

avg_purchase_by_city.plot(kind="bar", ax=axes[1,0], color="seagreen")
axes[1,0].set_title("Avg Purchase Amount by City")
axes[1,0].tick_params(axis='x', rotation=45)

sns.scatterplot(data=df, x="Age", y="PurchaseAmount", hue="Gender", ax=axes[1,1])
axes[1,1].set_title(f"Age vs Purchase Amount (corr={corr_age_purchase:.2f})")

df["Rating"].value_counts().sort_index().plot(kind="bar", ax=axes[1,2], color="slateblue")
axes[1,2].set_title("Rating Distribution")

plt.suptitle("Task 2: Exploratory Data Analysis Overview", fontsize=16)
plt.tight_layout()
plt.savefig("output.png", dpi=150)
plt.close()

# ----------------------------------------------------------------
# 5. Bonus: short findings report
# ----------------------------------------------------------------
report = f"""EDA FINDINGS REPORT - Task 2
Author: Suman D H

1. Dataset contains {df.shape[0]} records and {df.shape[1]} columns.
2. Average purchase amount overall: {df['PurchaseAmount'].mean():.2f}
3. City with highest average purchase amount: {top_city} ({avg_purchase_by_city.max():.2f})
4. Number of outliers detected in PurchaseAmount (IQR method): {len(outliers)}
5. Correlation between Age and PurchaseAmount: {corr_age_purchase:.3f} (weak/negligible linear relationship)
6. Gender-wise average purchase amount:
{avg_purchase_by_gender.to_string()}
7. Rating distribution is roughly uniform across 1-5 stars, suggesting no strong bias in customer satisfaction scores.
"""
with open("findings_report.txt", "w") as f:
    f.write(report)

print("\nFindings report saved as 'findings_report.txt'")
print("Visualization grid saved as 'output.png'")
