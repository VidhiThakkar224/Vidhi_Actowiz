from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List
import json

app=FastAPI()

client=MongoClient("mongodb://localhost:27017")

db=client["Dell_leptop"]
collection=db["leptop"]

new_db=client["dell_new_db"]
new_collection=new_db["products"]

class Product(BaseModel):
    category_url:str
    product_name:str
    product_url:str
    product_price:float
    product_images:List[str]

@app.get("/products/{product_url:path}")
def get_product(product_url:str):
    product=collection.find_one({"product_url":product_url},{"_id":0})
    if not product:
        return {"error":"product not found"}
    return product

@app.post("/products/import")
def import_products():

    with open("C:\Python Training\Dell\dell_scraped_data.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    if not products:
        return {"error": "No products found in JSON file"}

    new_collection.delete_many(products)

    for p in products:
        Product = Product(**p)
        new_collection.insert_one(products.dict())

    return {
        "message": f"{len(products)} products imported successfully"
    }