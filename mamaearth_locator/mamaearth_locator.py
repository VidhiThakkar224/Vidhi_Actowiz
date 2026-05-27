import json
from rich import print
from lxml import html
import requests

result = []
base_url = "https://mamaearth.in/mamaearth-store"

response = requests.get(base_url)
tree = html.fromstring(response.content)
mamaearth = tree.xpath ("//div[@class='sc-hwwEjo frtmmV']")
# for city in mamaearth:
#     result.append({
#         "city":city.xpath(".//div[@class='sc-kPVwWT yyylf']//p[@class='store-name']//text()")
#     })
print(mamaearth)

