import pandas as pd

df = pd.read_csv('supermarket_sales.csv')
print(df.head())

missing_values = df.isnull()
print(missing_values)

df['Date'] = pd.to_datetime(df['Date'])
numerical_columns = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'cogs', 'gross income', 'Rating']
df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric)
print(df.dtypes)

numerical_summary = df.describe()
print(numerical_summary)

product_categories = df['Product line'].value_counts()
sales_regions = df['City'].value_counts()
print(product_categories)
print(sales_regions)

df['Profit Margin'] = (df['gross income'] / df['cogs']) * 100
product_sales = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
region_sales = df.groupby('City')['Total'].sum().sort_values(ascending=False)
top_products = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
top_regions = df.groupby('City')['Total'].sum().sort_values(ascending=False)
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum()
monthly_sales_growth = monthly_sales.pct_change().fillna(0) * 100
print(top_products)
print(top_regions)
print(monthly_sales_growth)
