import pymongo
import json
from rich import print

"""
resource : 
---------
w3school : https://www.w3schools.com/python/python_mongodb_getstarted.asp
mongodb documentation : https://www.mongodb.com/docs/manual/reference/sql-comparison/ 
"""

with open(r'scraped_data/apple_tv_data.json', 'r') as f:
  products = json.load(f) 

# connect to the localhost server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# create database
mydb = myclient['Apple_TV']

# print(myclient.list_database_names())

# create table / collection
product_table =  mydb['apple_tv_movie_data']

product_table.delete_many({})


product_table.insert_many(products)


