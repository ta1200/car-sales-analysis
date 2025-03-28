import pandas as pd

# Load the dataset
df = pd.read_csv("car_sales_data.csv")

# Show the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Show basic summary stats
print("\nSummary statistics:")
print(df.describe())

# Show column names
print("\nColumn names:")
print(df.columns)

import matplotlib.pyplot as plt
import seaborn as sns

# Create a folder for charts (optional, if not already there)
import os
if not os.path.exists("charts"):
    os.makedirs("charts")

# Plot total profit by brand
plt.figure(figsize=(10,6))
sns.barplot(x="Brand", y="Profit", data=df, estimator=sum, ci=None)
plt.title("Total Profit by Car Brand")
plt.ylabel("Total Profit ($)")
plt.tight_layout()

# Save and show
plt.savefig("charts/profit_by_brand.png")
plt.show()


# Count number of sales per month
monthly_sales = df["Sale Month"].value_counts().reindex(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
)

# Plot monthly sales trend
plt.figure(figsize=(10,6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.title("Number of Cars Sold by Month")
plt.xlabel("Month")
plt.ylabel("Number of Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.show()


# Drop missing accessory data
df_accessory = df.dropna(subset=["Accessory"])

# Count most common accessories
accessory_counts = df_accessory["Accessory"].value_counts()

# Plot accessory popularity
plt.figure(figsize=(8,6))
sns.barplot(x=accessory_counts.values, y=accessory_counts.index)
plt.title("Most Frequently Sold Accessories")
plt.xlabel("Number of Sales")
plt.ylabel("Accessory")
plt.tight_layout()
plt.savefig("charts/accessory_popularity.png")
plt.show()
