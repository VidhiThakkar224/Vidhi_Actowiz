import json
import mysql.connector

# JSON load
with open(
    r"C:\Python Training\rockwestcomposites\rockwest_composites.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="rockwest_db"
)

cursor = conn.cursor()

# Product table query
product_query = """
INSERT INTO product_data(
    Product_name,
    Product_link,
    Product_SKU,
    Product_Price,
    Product_quntity
)
VALUES(%s,%s,%s,%s,%s)
"""

# Additional table query
additional_query = """
INSERT INTO additional_information(
    product_id,
    Application,
    Materials,
    Pattern,
    Angle_Corner_Style,
    Angle_Degree,
    Angle_Finish,
    Angle_Leg_Length,
    Angle_Thickness,
    Thickness,
    Length_Value,
    Length_max_continuous,
    Weight,
    Max_Operating_Temp,
    HTS_Code
)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for item in data:

    # quantity clean
    qty = item['product_quntity'].split(":")[-1]

    # price clean
    price = item['product_Price'].replace("$","")

    # insert product data
    product_values = (
        item['Product_name'],
        item['product_link'],
        item['product_SKU'],
        float(price),
        int(qty)
    )

    cursor.execute(product_query, product_values)

    # last inserted id
    product_id = cursor.lastrowid

    add = item['additional_information']

    # insert additional info
    additional_values = (
        product_id,
        add.get('Appliction'),
        add.get('Materials'),
        add.get('Pattern'),
        add.get('Angle Corner Style'),
        add.get('Angle Degree'),
        add.get('Angle Finish'),
        add.get('Angle Leg Length'),
        add.get('Angle Thickness'),
        add.get('Thickness'),
        add.get('Length'),
        add.get('Length (max continuous)'),
        add.get('Weight'),
        add.get('Max Operating Temp- (Tg)'),
        add.get('HTS - Harmonized Tariff Code')
    )

    cursor.execute(additional_query, additional_values)

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()