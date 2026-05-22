# import json
# from rich import print
# from lxml import html
# import requests

# result = []
# base_url = "https://mamaearth.in/mamaearth-store"

# response = requests.get(base_url)
# tree = html.fromstring(response.content)
# mamaearth = tree.xpath ("//p[@class='store-name']/text()")
# # for city in mamaearth:
# #     result.append({
# #         "city":city.xpath(".//div[@class='sc-kPVwWT yyylf']//p[@class='store-name']//text()")
# #     })
# print(response.text)

import requests
from lxml import html
from rich import print

url = "https://mamaearth.in/mamaearth-store"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

tree = html.fromstring(response.content)

stores = tree.xpath('//div[contains(@class,"store-card")]')

result = []

for store in stores:

    store_name = store.xpath('.//p/text()')
    details = store.xpath('.//text()')

    clean_data = [i.strip() for i in details if i.strip()]

    result.append({
        "store_name": clean_data[0] if len(clean_data) > 0 else None,
        "address": clean_data[1] if len(clean_data) > 1 else None,
        "timing": clean_data[2] if len(clean_data) > 2 else None,
        "phone": clean_data[3] if len(clean_data) > 3 else None,
        "email": clean_data[4] if len(clean_data) > 4 else None
    })

print(result)