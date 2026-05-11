SELECT * FROM menu_items;

CREATE DATABASE IF NOT EXISTS zometo;
USE zometo;

DROP TABLE IF EXISTS zometo_restaurant_data;

CREATE TABLE zometo_restaurant_data (
    category_name VARCHAR(255),
    item_id VARCHAR(255),
    item_name VARCHAR(255),
    item_description TEXT,
    item_price FLOAT,
    is_veg BOOLEAN
);

select * from zometo_restaurant_data;
drop table zometo.zometo_restaurent_data;

SHOW TABLES;