import pandas as pd
import numpy as np
np.random.seed(42)

n = 300
names = [f"Customer_{i}" for i in range(1, n+1)]
ages = np.random.randint(18, 70, n).astype(float)
genders = np.random.choice(["Male", "Female", "male", "FEMALE", "M", "F"], n)
cities = np.random.choice(["Bangalore", "bangalore", "Mumbai", "MUMBAI", "Delhi", "Chennai", "Hyderabad", None], n)
purchase_amount = np.round(np.random.uniform(100, 5000, n), 2)
signup_date = pd.date_range("2023-01-01", periods=n, freq="D").astype(str)
rating = np.random.choice([1,2,3,4,5, np.nan], n)

df = pd.DataFrame({
    "CustomerID": range(1, n+1),
    "Name": names,
    "Age": ages,
    "Gender": genders,
    "City": cities,
    "PurchaseAmount": purchase_amount,
    "SignupDate": signup_date,
    "Rating": rating
})
df["Age"] = df["Age"].astype(object)

# Inject missing values
for col in ["Age", "PurchaseAmount", "Rating", "City"]:
    idx = np.random.choice(df.index, size=int(n*0.08), replace=False)
    df.loc[idx, col] = np.nan

# Inject duplicate rows
dupes = df.sample(15, random_state=1)
df = pd.concat([df, dupes], ignore_index=True)

# Inject inconsistent data types (age as string for some rows)
str_idx = np.random.choice(df.index, size=10, replace=False)
for i in str_idx:
    val = df.at[i, "Age"]
    if pd.notna(val):
        df.at[i, "Age"] = str(val)

df.to_csv("customer_data_raw.csv", index=False)
print("Raw dataset created:", df.shape)
