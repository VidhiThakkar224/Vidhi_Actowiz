# import requests
import json
from lxml import html
from rich import print

# url='https://www.dominos.co.in/store-location/'
# response=requests.get(url)

with open(r"C:\Python Training\Domino's_locator\Dominos_location.html", "r", encoding='utf-8') as f:
    data = f.read()
    result = []

    tree=html.fromstring(data)
    parent_class=tree.xpath("//div[@class='row']")
    for data in parent_class:
        result.append({
            "outlet_url":data.xpath(".//div[@class='media-body']//a/@href")
            

        })
print(result)