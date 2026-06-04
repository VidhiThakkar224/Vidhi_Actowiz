import json
import pymongo
from rich import print

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mamaearth_store_locator"]
mycol = mydb["all_information"]
mycol.delete_many({}) 

with open ("C:\Python Training\mamaearth_locator\mamaearth_data.json","r",encoding="utf-8")as f:
    data = json.load(f)

try:
    mycol.insert_many(data)
    print("Data inserted")
except Exception as e:
    print("Dupliced product skipped")
    print(e)