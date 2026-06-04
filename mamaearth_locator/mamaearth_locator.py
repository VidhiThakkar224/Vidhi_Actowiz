import json
from rich import print
from lxml import html
import requests
import jmespath

with open(r"C:\Python Training\mamaearth_locator\mamaearth_store.json","r",encoding="utf-8")as f:
    data = json.load(f)
result = []
base_url = "https://mamaearth.in/mamaearth-store"

response = requests.get(base_url)
tree = html.fromstring(response.content)

# print(type(location_number))
mamaearth = jmespath.search("data[]",data)

for info in mamaearth:
    location_number = jmespath.search("store_latLong",data)
    # loction = ', '.join(location_number)

    result.append({

            "city":jmespath.search("store_city",info),
            "location":jmespath.search("store_location",info),
            "address":jmespath.search("store_address",info),
            "store_open_time":jmespath.search("store_timing",info),
            "store_contactNumber":jmespath.search("store_contactNumber",info),
            "store_email":jmespath.search("store_email",info),
            "direction_url":f"https://www.google.com/maps/dir/{location_number}/@22.9980939,72.5019839,14z/data=!3m1!4b1!4m2!4m1!3e0?entry=ttu&g_ep=EgoyMDI2MDYwMS4wIKXMDSoASAFQAw%3D%3D"

            })
print(result)
# print(location_number)

with open ("C:\Python Training\mamaearth_locator\mamaearth_data.json","w",encoding="utf-8")as f:
    json.dump(result,f,indent=4)