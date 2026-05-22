import mysql.connector
import json

with open(r'C:\Python Training\Day12\harrisfarm_data.json', 'r', encoding='utf-8') as f:
    restaurant_data = json.load(f)

# Database connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="harrisfarm"
)

cursor = conn.cursor()

# Create table
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            category_name VARCHAR(255),
            category_link TEXT
        )
    """)

except Exception as e:
    print("Error :", e)

# Insert query
query = """
INSERT INTO categories (
    category_name,
    category_link
)
VALUES (%s, %s)
"""

# Data insert
for item in restaurant_data:

    category_name = item.get("category_name")
    category_link = item.get("category_link")

    values = (category_name, category_link)

    cursor.execute(query, values)

    print("Data inserted successfully")

# Close connection
conn.commit()
conn.close()