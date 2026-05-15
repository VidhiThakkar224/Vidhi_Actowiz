import mysql.connector

# Database connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="harrisfarm"
)

# Cursor create
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

    print("Table created successfully")

except Exception as e:
    print("Error :", e)

# Save changes
conn.commit()

# Close connection
cursor.close()
conn.close()