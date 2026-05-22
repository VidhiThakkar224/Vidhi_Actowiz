import json
from rich import print
from lxml import html
import requests

result = []
base_url = "https://www.rockwestcomposites.com/808-150-12.html/"

response = requests.get(base_url)
tree = html.fromstring(response.content)
rockwest = tree.xpath("//div[@class='product-detail product-wrapper single-product']")

for data in rockwest:
    result.append({
        "Product_name":data.xpath(".//div[@class='row']//h1[@class='product-name']//text()")[0],
        "product_link":"https://www.rockwestcomposites.com/808-150-12.html",
        "product_SKU":data.xpath(".//div[@class='product-detail-right']//span[@class='product-id product-sku']//text()")[0].replace("\n","").replace(" ","").strip(),
        "product_Price":data.xpath(".//div[@class='price']//span[@class='sales default-price']//text()")[1].strip(),
        "product_quntity":data.xpath(".//div[@class='product-availability pull-right']//span[@class='product-stock-availability']//text()")[0].replace("\n","").replace(" ","").strip(),        "product_length":data.xpath(".//div[@class='product-detail-right']//h2[@class='product-short-title']//text()")[0],
        "additional_information":{
            "Appliction":data.xpath(".//tr[th='Application']/td[@class='has-value']/span/text()")[0],
            "Materials":data.xpath(".//tr[th='Materials']/td[@class='has-value']/span/text()")[0],
            "Pattern":data.xpath(".//tr[th='Pattern']/td[@class='has-value']/span/text()")[0],
            "Angle Corner Style":data.xpath(".//tr[th='Angle Corner Style']/td[@class='has-value']/span/text()")[0],
            "Angle Degree":data.xpath(".//tr[th='Angle Degree']/td[@class='has-value']/span/text()")[0],
            "Angle Finish":data.xpath(".//tr[th='Angle Finish']/td[@class='has-value']/span/text()")[0],
            "Angle Leg Length":data.xpath(".//tr[th='Angle Leg Length']/td[@class='has-value']/span/text()")[0],
            "Angle Thickness":data.xpath(".//tr[th='Angle Thickness']/td[@class='has-value']/span/text()")[0],
            "Thickness":data.xpath(".//tr[th='Thickness']/td[@class='has-value']/span/text()")[0],
            "Length":data.xpath(".//tr[th='Length']/td[@class='has-value']/span/text()")[0],
            "Length (max continuous)":data.xpath(".//tr[th='Length (max continuous)']/td[@class='has-value']/span/text()")[0],
            "Weight":data.xpath(".//tr[th='Weight']/td[@class='has-value']/span/text()")[0],
            "Max Operating Temp- (Tg)":data.xpath(".//tr[th='Max Operating Temp- (Tg)']/td[@class='has-value']/span/text()")[0],
            "HTS - Harmonized Tariff Code":data.xpath(".//tr[th='HTS - Harmonized Tariff Code']/td[@class='has-value']/span/text()")[0],
        }
    })

print(result)

with open("rockwest_composites.json","w",encoding='utf 8') as f:
    json.dump(result, f, indent = 4)
