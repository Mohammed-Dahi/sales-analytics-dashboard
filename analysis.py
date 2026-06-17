import pandas as pd

try:
    df = pd.read_csv('raw-sales-data.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'raw-sales-data.csv' was not found.")


print("First 5 rows of the dataset:")
print(df.head())

print("\n---Data Info---")
print(df.info())

# clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
print("\n---Cleaned Column Names---")
print(df.columns)


# convert date column to datetime format
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
print("\n---Converted 'order_date' to datetime format---")
print(df['order_date'])

# Feature Engineering
df['order-year'] = df['order_date'].dt.year
df['order-month'] = df['order_date'].dt.strftime('%B')
df['order_month_number'] = df['order_date'].dt.month

# Profit Margin
df['profit_margin'] = (df['profit'] / df['sales']) * 100
print("\n---Profit Margin---")
print(df['profit_margin'])

# Show Data After Feature Engineering
print("\n---Data After Feature Engineering---")
print(df.head())
print("\n---Data Info After Feature Engineering---")
print(df.info())

# Phase 2: EDA (Exploratory Data Analysis)

print("\n" + "=" * 50)
print("Exploratory Data Analysis (EDA)")
print("=" * 50)

# Core KPIs
total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
total_quantity = df['quantity'].sum()
avg_margin = (total_profit / total_sales) * 100

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Profit Margin: {avg_margin:.2f}%")

# Regional Performance

print("\n---Regional Performance---")
region_analysis = df.groupby('region').agg(
    total_sales=('sales', 'sum'),
    total_profit=('profit', 'sum'),
    avg_discount=('discount', 'mean')
).sort_values(by='total_profit', ascending=False)
print(region_analysis)

# product sub-category performance

print("\n---Product Sub-Category Performance---")
sub_category_analysis = df.groupby(['category', 'sub-category']).agg(
    total_sales=('sales', 'sum'),
    total_profit=('profit', 'sum')
).sort_values(by='total_profit', ascending=False).head(10)
print(sub_category_analysis)

# Time Series Analysis

print("\n---Time Series Analysis---")
yearly_analysis = df.groupby('order-year').agg(
    total_sales=('sales', 'sum'),
    total_profit=('profit', 'sum')
)
print(yearly_analysis)