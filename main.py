import pandas as pd
import sqlite3

print("🚀 Script started...")

df = pd.read_csv("data.csv")
print("📄 CSV loaded")

df['price'] = df['price'].fillna(0)
df['quantity'] = df['quantity'].fillna(1)

df['revenue'] = df['price'] * df['quantity']
print("🧹 Data cleaned")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("🎉 DONE! Data stored in SQLite")

df2 = pd.read_sql("SELECT * FROM sales", conn)
print("\n📊 Data from Database:")
print(df2)

print("🎉 DONE! Data stored in SQLite")

# 📊 Read data from database
df2 = pd.read_sql("SELECT * FROM sales", conn)
print("\n📊 Full Data:")
print(df2)

# 💰 Total Revenue
result = pd.read_sql("SELECT SUM(revenue) FROM sales", conn)
print("\n💰 Total Revenue:")
print(result)

# 📦 Product-wise revenue
result = pd.read_sql("""
SELECT product, SUM(revenue) as total_revenue
FROM sales
GROUP BY product
""", conn)

print("\n📦 Revenue by Product:")
print(result)

# 🏆 Top product
result = pd.read_sql("""
SELECT product, SUM(revenue) as total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 1
""", conn)

print("\n🏆 Top Product:")
print(result)

result = pd.read_sql("""
SELECT product, COUNT(*) as total_orders
FROM sales
GROUP BY product
""", conn)

print("\n📊 Number of orders per product:")
print(result)