import mysql.connector
import json

with open(r'C:\Python Training\Day7\Zomato_data.json', 'r', encoding='utf-8') as f:
    restaurant_data = json.load(f)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="zometo"
)

cursor = conn.cursor()

query = """
INSERT INTO zometo_restaurant_data (
    category_name,
    item_id,
    item_name,
    item_description,
    item_price,
    is_veg
)
VALUES (%s, %s, %s, %s, %s, %s)
"""

count = 0

for restaurant in restaurant_data:

    for category in restaurant['menu_categories']:

        for item in category['items']:

            values = (
                category['category_name'],
                str(item['id']),
                item['name'],
                item['item_description'],
                float(item['item_price']),
                bool(item['is_veg'])
            )

            cursor.execute(query, values)

            count += 1

conn.commit()

print(f"{count} rows inserted successfully!")

cursor.execute("SELECT COUNT(*) FROM zometo_restaurant_data")

result = cursor.fetchone()

print("Total Rows In Database =", result[0])

cursor.close()
conn.close()