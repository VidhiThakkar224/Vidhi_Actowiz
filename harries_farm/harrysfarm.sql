CREATE DATABASE harrisfarm;
SHOW DATABASES;

CREATE TABLE IF NOT EXISTS categories (
    category_name VARCHAR(255),
    category_link TEXT
);

select * from harrisfarm.categories;

drop table categories;