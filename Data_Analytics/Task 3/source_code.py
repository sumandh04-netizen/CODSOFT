"""
Task 3: Data Visualization Dashboard
CodSoft Data Analytics Internship
Author: Suman D H

Steps performed:
1. Create meaningful visualizations using Matplotlib & Seaborn
2. Bar, line, pie, histogram, scatter charts
3. Customize with titles, labels, legends, color schemes
4. Combine into a single dashboard-style output image
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
df = pd.read_csv("sales_dataset.csv")
df["SignupDate"] = pd.to_datetime(df["SignupDate"])
df["SignupMonth"] = df["SignupDate"].dt.to_period("M").astype(str)

fig, axes = plt.subplots(2, 3, figsize=(20, 11))
fig.suptitle("CodSoft Data Analytics - Sales Dashboard", fontsize=18, fontweight="bold")

# 1. Bar chart - Avg purchase by city
city_avg = df.groupby("City")["PurchaseAmount"].mean().sort_values(ascending=False)
sns.barplot(x=city_avg.index, y=city_avg.values, ax=axes[0,0], palette="viridis")
axes[0,0].set_title("Average Purchase Amount by City")
axes[0,0].set_ylabel("Avg Purchase Amount (₹)")
axes[0,0].set_xlabel("City")
axes[0,0].tick_params(axis='x', rotation=40)

# 2. Line chart - monthly signups trend
monthly_signups = df.groupby("SignupMonth").size()
axes[0,1].plot(monthly_signups.index, monthly_signups.values, marker="o", color="teal", linewidth=2)
axes[0,1].set_title("Monthly Customer Signups Trend")
axes[0,1].set_ylabel("New Signups")
axes[0,1].set_xlabel("Month")
axes[0,1].tick_params(axis='x', rotation=60)

# 3. Pie chart - Gender distribution
gender_counts = df["Gender"].value_counts()
axes[0,2].pie(gender_counts.values, labels=gender_counts.index, autopct="%1.1f%%",
              colors=["#66b3ff", "#ff9999"], startangle=90)
axes[0,2].set_title("Customer Gender Distribution")

# 4. Histogram - Purchase amount distribution
axes[1,0].hist(df["PurchaseAmount"], bins=25, color="darkorange", edgecolor="black")
axes[1,0].set_title("Purchase Amount Distribution")
axes[1,0].set_xlabel("Purchase Amount (₹)")
axes[1,0].set_ylabel("Frequency")

# 5. Scatter plot - Age vs Purchase amount colored by rating
scatter = axes[1,1].scatter(df["Age"], df["PurchaseAmount"], c=df["Rating"], cmap="cool", alpha=0.7)
axes[1,1].set_title("Age vs Purchase Amount (colored by Rating)")
axes[1,1].set_xlabel("Age")
axes[1,1].set_ylabel("Purchase Amount (₹)")
legend1 = axes[1,1].legend(*scatter.legend_elements(), title="Rating", loc="upper right", fontsize=8)
axes[1,1].add_artist(legend1)

# 6. Bar chart - Rating counts
rating_counts = df["Rating"].value_counts().sort_index()
sns.barplot(x=rating_counts.index, y=rating_counts.values, ax=axes[1,2], palette="magma")
axes[1,2].set_title("Customer Rating Counts")
axes[1,2].set_xlabel("Rating (stars)")
axes[1,2].set_ylabel("Number of Customers")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("output.png", dpi=150)
plt.close()

print("Dashboard saved as 'output.png'")
