"""
Task 4: Customer Data Analysis
CodSoft Data Analytics Internship
Author: Suman D H

Steps performed:
1. Analyze customer information to understand purchasing behavior
2. Segment customers by age, location, buying patterns
3. Identify most valuable customer groups
4. Create visual reports
5. Bonus: Marketing strategy suggestions (see marketing_strategy.txt)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv("customer_dataset.csv")

# ----------------------------------------------------------------
# 1. Purchasing behavior overview
# ----------------------------------------------------------------
print("Purchase amount summary:\n", df["PurchaseAmount"].describe())

# ----------------------------------------------------------------
# 2. Segment customers by age group
# ----------------------------------------------------------------
bins = [17, 25, 35, 45, 55, 70]
labels = ["18-25", "26-35", "36-45", "46-55", "56-70"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

segment_summary = df.groupby("AgeGroup", observed=True).agg(
    CustomerCount=("CustomerID", "count"),
    AvgPurchase=("PurchaseAmount", "mean"),
    TotalPurchase=("PurchaseAmount", "sum")
).round(2)
print("\nSegment summary by age group:\n", segment_summary)

# Segment by city
city_summary = df.groupby("City").agg(
    CustomerCount=("CustomerID", "count"),
    AvgPurchase=("PurchaseAmount", "mean"),
    TotalPurchase=("PurchaseAmount", "sum")
).round(2).sort_values("TotalPurchase", ascending=False)
print("\nSegment summary by city:\n", city_summary)

# ----------------------------------------------------------------
# 3. Identify most valuable customer groups (top 10% spenders)
# ----------------------------------------------------------------
threshold = df["PurchaseAmount"].quantile(0.90)
high_value_customers = df[df["PurchaseAmount"] >= threshold]
print(f"\nHigh-value customers (top 10%, spend >= {threshold:.2f}): {len(high_value_customers)}")
high_value_customers[["CustomerID","Name","Age","City","PurchaseAmount","Rating"]]\
    .sort_values("PurchaseAmount", ascending=False)\
    .to_csv("high_value_customers.csv", index=False)

# ----------------------------------------------------------------
# 4. Visual reports (output.png)
# ----------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Task 4: Customer Segmentation & Insights", fontsize=16, fontweight="bold")

segment_summary["CustomerCount"].plot(kind="bar", ax=axes[0,0], color="cornflowerblue")
axes[0,0].set_title("Customer Count by Age Group")
axes[0,0].set_ylabel("Number of Customers")

segment_summary["AvgPurchase"].plot(kind="bar", ax=axes[0,1], color="salmon")
axes[0,1].set_title("Average Purchase Amount by Age Group")
axes[0,1].set_ylabel("Avg Purchase (₹)")

city_summary["TotalPurchase"].plot(kind="bar", ax=axes[1,0], color="seagreen")
axes[1,0].set_title("Total Revenue by City")
axes[1,0].set_ylabel("Total Purchase (₹)")
axes[1,0].tick_params(axis='x', rotation=40)

axes[1,1].scatter(df["Age"], df["PurchaseAmount"], alpha=0.4, label="All Customers", color="gray")
axes[1,1].scatter(high_value_customers["Age"], high_value_customers["PurchaseAmount"],
                   color="crimson", label="High-Value (Top 10%)")
axes[1,1].set_title("High-Value Customers Highlighted")
axes[1,1].set_xlabel("Age")
axes[1,1].set_ylabel("Purchase Amount (₹)")
axes[1,1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("output.png", dpi=150)
plt.close()

# ----------------------------------------------------------------
# 5. Bonus: Marketing strategy suggestions
# ----------------------------------------------------------------
top_city = city_summary["TotalPurchase"].idxmax()
top_age_group = segment_summary["AvgPurchase"].idxmax()

strategy = f"""MARKETING STRATEGY SUGGESTIONS - Task 4
Author: Suman D H

1. Focus loyalty campaigns on the '{top_age_group}' age group, which shows the
   highest average purchase amount.
2. '{top_city}' generates the highest total revenue - prioritize regional
   promotions and faster delivery/support in this city.
3. Target the identified {len(high_value_customers)} high-value customers (top 10% spenders)
   with exclusive offers and early access to new products to improve retention.
4. Consider re-engagement email campaigns for low-activity customer segments
   to increase overall purchase frequency.
5. Use rating data to identify dissatisfied customers (rating <= 2) for
   proactive customer service outreach.
"""
with open("marketing_strategy.txt", "w") as f:
    f.write(strategy)

print("\nHigh value customers saved as 'high_value_customers.csv'")
print("Marketing strategy saved as 'marketing_strategy.txt'")
print("Visual report saved as 'output.png'")
