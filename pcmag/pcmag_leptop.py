import json
from rich import print
from lxml import html
from curl_cffi import requests

response = requests.get("https://www.pcmag.com/picks/the-best-laptops",impersonate="chrome120")
# response = requests.get("https://www.pcmag.com/picks/the-best-tvs",impersonate="chrome120")
data=response.content.decode('utf-8')

result = []
tree = html.fromstring(data)

url = "https://www.pcmag.com"

products=tree.xpath("//div[contains(@class, 'flex flex-col gap-6')]//div[contains(@class, 'flex flex-col gap-y-6')]")

for data in products:
    heading = data.xpath(".//div[contains(@class,'flex flex-wrap items-center justify-start text-sm font-bold leading-tight')]/text()")
    product_name =data.xpath(".//h3[@class='font-stretch-condensed line-clamp-3 text-base font-bold leading-tight md:w-full']//a/text()")
    product_url = data.xpath(".//h3[@class='font-stretch-condensed line-clamp-3 text-base font-bold leading-tight md:w-full']//a/@href")
    product_img = data.xpath(".//img[@class = 'order-last aspect-video w-[120px] border border-gray-300 md:order-first']//@data-image-loader")
    price= data.xpath(".//span[@class='inline-block']/text()")
    description = data.xpath(".//p[@class = 'text-sm leading-normal']/text()")
    pros = [d.strip() for d in data.xpath(".//h4[contains(text(),'Pros')]/following-sibling::ul//li//span/text()")if d.strip()]
    cons = [d.strip() for d in data.xpath(".//h4[contains(text(),'Cons')]/following-sibling::ul//li//span/text()")if d.strip()]
    rating = data.xpath(".//div[@class = 'text-sm']/text()")
    review = data.xpath(".//a[@class='inline-flex w-fit text-sm font-bold text-red-400 underline hover:text-red-500']/@href")

    result.append({
        "heading":heading[0].strip() if heading else None,
        "product_name":product_name[0].strip(),
        "product_url":product_url[0].strip(),
        "image_url":product_img,
        "product_price":price[0].strip().split('$')[1],
        "product_description":description,
        "pros":pros,
        "cons":cons,
        "rating":rating[0],
        "review":url+review[0] if review else None
    })

print(result)

with open("C:\Python Training\pcmag\pcmag_leptop_data.json","w",encoding='utf 8') as f:
    json.dump(result, f, indent = 4)