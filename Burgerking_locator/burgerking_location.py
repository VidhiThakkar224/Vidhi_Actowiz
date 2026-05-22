import json
from rich import print
from lxml import html

with open(r'C:\Python Training\Day12\burgerking_location.html', "r", encoding='utf-8') as f:
    data = f.read()
    result = []
    
    tree = html.fromstring(data)
    parent_class = tree.xpath("//div[@class='store-info-box']/ul")
    for data in parent_class:
        result.append({
        "name" : data.xpath('./li[@class="outlet-name"]//div[@class="info-text"]/a//text()')[0],
        "address": ' '.join(x.replace(" ", "").replace("\n", "").strip() for x in data.xpath('./li[@class="outlet-address"]//div[@class="info-text"]//span//text()')).split("-")[0],
        "pincode":  data.xpath('./li[@class="outlet-address"]//div[@class="info-text"]//span//text()')[-1],
        "phone_number": data.xpath('./li[@class="outlet-phone"]//div[@class="info-text"]/a//text()')[0],
        "time": data.xpath('./li[@class="outlet-timings"]//div[@class="info-text"]//span/text()')[0],
        "map": data.xpath('./li[@class="outlet-actions"]//a[@class="btn btn-map"]//@href')[0],
        "website": data.xpath('./li[@class="outlet-actions"]//a[@class="btn btn-website"]//@href')[0]
                })

print(result)

with open('burgerking_location_data.json', 'w', encoding='utf-8') as f:
  json.dump(result, f, indent=4)