CREATE DATABASE zomato_db;
USE zomato_db;

CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id VARCHAR(100),
    restaurant_name VARCHAR(255),
    category_name VARCHAR(255),
    item_id VARCHAR(100),
    item_name VARCHAR(255),
    item_description TEXT,
    item_price FLOAT,
    is_veg BOOLEAN
);

SELECT * FROM menu_items;