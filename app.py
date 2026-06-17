import streamlit as st
import pandas as pd
import plotly.express as px

# Page Settings
st.set_page_config(page_title="Sales Data Analysis", layout="wide")
st.title("Sales Data Analysis Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('raw-sales-data.csv')
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', '_', regex=True)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['order-year'] = df['order_date'].dt.year
    df['order-month'] = df['order_date'].dt.strftime('%B')
    df['profit_margin'] = (df['profit'] / df['sales']) * 100
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
years = df['order-year'].unique()
selected_year = st.sidebar.selectbox("Select Year", years)
regions = df['region'].unique()
selected_region = st.sidebar.multiselect("Select Region(s)", regions, default=regions)

# Filter Data Based on Selections
filtered_df = df[(df['order-year'] == selected_year) & (df['region'].isin(selected_region))]

# Display KPIs
st.subheader("Key Performance Indicators (KPIs)")
total_sales = filtered_df['sales'].sum()
total_profit = filtered_df['profit'].sum()
total_quantity = filtered_df['quantity'].sum()
avg_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Quantity Sold", f"{total_quantity}")
col4.metric("Average Profit Margin", f"{avg_margin:.2f}%")

st.markdown("---")

# Interactive Visualizations
st.subheader("Sales and Profit Over Time")
# Line Chart for Sales and Profit Over Time
sales_profit_fig = px.line(filtered_df, x='order_date', y=['sales', 'profit'], title='Sales and Profit Over Time', labels={'value': 'Amount', 'order_date': 'Order Date'})
st.plotly_chart(sales_profit_fig, use_container_width=True)

# Bar Chart for Sales by Region
st.subheader("Sales by Region")
sales_by_region = filtered_df.groupby('region')['sales'].sum().reset_index()
sales_region_fig = px.bar(sales_by_region, x='region', y='sales', title='Sales by Region', labels={'sales': 'Total Sales', 'region': 'Region'})
st.plotly_chart(sales_region_fig, use_container_width=True)

# Pie Chart for Profit Margin by Region
st.subheader("Profit Margin by Region")
profit_margin_by_region = filtered_df.groupby('region')['profit_margin'].mean().reset_index()
profit_margin_fig = px.pie(profit_margin_by_region, names='region', values='profit_margin', title='Average Profit Margin by Region')
st.plotly_chart(profit_margin_fig, use_container_width=True)

# Additional Insights
st.subheader("Additional Insights")

# Time Series Analysis
st.subheader("Time Series Analysis")
yearly_analysis = filtered_df.groupby('order-year').agg(
    total_sales=('sales', 'sum'),
    total_profit=('profit', 'sum')).reset_index()
yearly_fig = px.bar(yearly_analysis, x='order-year', y=['total_sales', 'total_profit'], title='Yearly Sales and Profit', labels={'value': 'Amount', 'order-year': 'Year'})
st.plotly_chart(yearly_fig, use_container_width=True)

# End of Dashboard
