import pandas as pd
import sqlite3
orders = pd.read_csv("orders.csv")
users = pd.read_json("users.json")
conn = sqlite3.connect(":memory:")
with open("restaurants.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())

restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)
df = orders.merge(users, on="user_id", how="left")
df = df.merge(restaurants, on="restaurant_id", how="left")
df.to_csv("final_food_delivery_dataset.csv", index=False)

print("✅ Final dataset created successfully!") 