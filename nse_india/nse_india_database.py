import pymongo
import json
from rich import print
import jmespath

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["nse_india"]
mycol = mydb["sectoral_indicies"]
mycol.delete_many({})  
top = mydb["TOP_20_shares"]
top.delete_many({})  
bottom = mydb["BOTTOM_20_shares"]
bottom.delete_many({})   
# mycol.create_index("order_code",unique=True)

#high and low 20 shares

with open (r"C:\Python Training\nse_india\sectoral_indices_stock_data.json",'r',encoding='utf-8') as f:
    new_data=json.load(f)

    all_stocks = jmespath.search("[*].sectoral_data[]", new_data)
    # print(all_stocks)

    seen = set()
    unique_stocks = []
    for stock in all_stocks:
        if stock["symbol"] not in seen:
            seen.add(stock["symbol"])
            unique_stocks.append(stock)

    top_20_gainers = sorted(unique_stocks, key=lambda x: x["change_percentage"] or 0, reverse=True)[:20]
    bottom_20_losers = sorted(unique_stocks, key=lambda x: x["change_percentage"] or 0, reverse=False)[:20]

    print(top_20_gainers)
    print(bottom_20_losers)

    top.insert_many(top_20_gainers)
    bottom.insert_many(bottom_20_losers)

try:
    mycol.insert_many(new_data)
    print("Data inserted")
except Exception as e:
    print("Dupliced product skipped")
    print(e)