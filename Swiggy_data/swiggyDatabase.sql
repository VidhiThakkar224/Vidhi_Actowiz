create database swiggy_data;
create table swiggy_data.swiggy_restaurent_data(
		restaurent_name varchar(255),
		itemname varchar(255),
		image_url text,
		price float,
		final_price float,
        discount float,
		ratings varchar(255),
		restaurent_avg_rating float,
		isVag bool,
		rating_count varchar(255),
        offers text,
        restaurent_url text,
        restaurent_address text
        )
        
select * from swiggy_data.swiggy_restaurent_data;

drop table swiggy_data.swiggy_restaurent_data;