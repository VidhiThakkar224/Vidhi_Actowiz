import pymongo
import json
from rich import print

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Dell_leptop"]
mycol = mydb["leptop"]
mycol.delete_many({})   
# mycol.create_index("order_code",unique=True)

with open (r"C:\Python Training\Dell\dell_scraped_data.json","r",encoding= "utf-8")as f:
    data = json.load(f)

try:
    mycol.insert_many(data)
    print("Data inserted")
except Exception as e:
    print("Dupliced product skipped")
    print(e)