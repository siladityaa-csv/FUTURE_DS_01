#loading & cleaning data--
import pandas as pd

df = pd.read_csv("Superstore.csv", encoding='latin1')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Remove duplicates
df = df.drop_duplicates()

# Create Year & Month columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Year-Month'] = df['Order Date'].dt.to_period('M')

print(df.info())
print ("\n ")


#KPI Calculations
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Avg Order Value:", avg_order_value)
print("Profit Margin %:", profit_margin)

monthly_sales = df.groupby('Year-Month')['Sales'].sum()
monthly_profit = df.groupby('Year-Month')['Profit'].sum()

monthly_sales.plot(figsize=(12,6), title="Monthly Sales Trend")

#For top 10 product 
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("Top 10 Products by Sales")
print(top_products)
top_profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Profit")
print (top_profit_products)

#For category Analysis
category_sales = df.groupby('Category')['Sales'].sum()
category_profit = df.groupby('Category')['Profit'].sum()
category_margin = (category_profit / category_sales) * 100
#relegion bassed
region_sales = df.groupby('Region')['Sales'].sum()
region_profit = df.groupby('Region')['Profit'].sum()

region_margin = (region_profit / region_sales) * 100

df.to_csv("cleaned_superstore.csv", index=False)