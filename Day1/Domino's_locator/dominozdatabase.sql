create database dominoz_db;
use dominoz_db;
create table pizza_data(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    pizza_name varchar(255),
    Restaurant_link text,
    image_link text,
    city_name varchar(255),
    address varchar(255),
    pincode int,
    delivery_in varchar(255),
    cost varchar(255),
    hours varchar(255),
    good_for varchar(255),
    phone_number int,
    view_menu text,
    order_now text
);
drop table pizza_data;
select * from dominoz_db.pizza_data;
show tables;