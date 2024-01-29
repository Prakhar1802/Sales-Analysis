"""
Project Name: Sales data Analysis
Project data source: MeriSkill
Project Creator: Prakhar Tripathi

Purpose: Analyze sales data to identify trends, top-selling products, and revenue metrics
for business decision-making.

Description: In this project, you will dive into a large sales dataset to extract
valuable insights. You will explore sales trends over time, identify the best-selling products, calculate revenue
metrics such as total sales and profit margins, and create visualizations to present your findings effectively. This
project showcases your ability to manipulate and derive insights from large datasets, enabling you to make
data-driven recommendations for optimizing sales strategies.

"""

import pandas as pd
import matplotlib.pyplot as plt

# Importing the sales dataset
data = pd.read_csv("C:\\Users\\prakh\\Downloads\\Practice DataSet\\Sales Data.csv")

# checking the dataset
print(data.head())

# Checking the column of the dataset
print(data.columns)

# Removing the unused columns from dataset
data.drop(["Unnamed: 0", "Hour", "Month", "Order ID"], axis=1, inplace=True)
print(data.columns)

# Checking the summary of data
print(data.describe())

# Checking the null values in dataset
print(data.info())

# Changing the datatype of Order Date
data["Order Date"] = pd.to_datetime(data["Order Date"])

# Plotting a graph that show the count of products by cities
product_count = data.groupby("City").size()
plt.figure(figsize=(18, 7))
plt.bar(product_count.index, product_count.values, color="lightgreen")
plt.xlabel("City")
plt.ylabel("Count of Products")
plt.title("Count of products by cities")
plt.show()

# Sales of all Products
unique_products = data["Product"].unique()
product_price = data.groupby('Product')['Price Each'].sum()
plt.figure(figsize=(18, 7))
plt.bar(unique_products, product_price, color="lightblue")
plt.xlabel("Products")
plt.xticks(rotation='vertical')
plt.ylabel("Total amount in Millions")
plt.title("Sales of all Products")
plt.show()

# Maximum Quantity ordered by customers
quantity = data["Quantity Ordered"].value_counts()
plt.figure(figsize=(18, 7))
plt.bar(quantity.index, quantity.values, color="yellow")
plt.xlabel("Number of Quantity")
plt.ylabel("Count")
plt.title("Quantity ordered by customers")
plt.show()

# Sales in Cities
sales_count = data.groupby('City')['Sales'].size()
plt.figure(figsize=(18, 7))
plt.plot(sales_count.index, sales_count.values, color="orange")
plt.xlabel("City")
plt.ylabel("Sales Count")
plt.title("Sales count per city")
plt.show()

# Product Counts
products = data["Product"].value_counts()
plt.figure(figsize=(18, 7))
plt.bar(products.index, products.values, color="purple")
plt.xlabel("Products")
plt.xticks(rotation='vertical')
plt.ylabel("Count")
plt.title("Product Count")
plt.show()
