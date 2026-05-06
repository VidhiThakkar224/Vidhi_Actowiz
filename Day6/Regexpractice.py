import re
url = "https://books.toscrape.com/"
with open('Day6/booktoscrapeDATA.html', "r", encoding='utf-8') as f:
    data = f.read()
# email_pattern = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",data)
page = re.findall(r'href="([^"]+\.html)"',data)
img = re.findall(r'src="([^"]+\.jpg)"',data)
img_url = [url + img for img in img]
name = re.findall(r'title="([^"]+)"',data)
price = re.findall(r"£\d.+[0-9]",data)
print("-------------------------------------------     PRICE     -------------------------------------------")
print(price)

print("-------------------------------------------     NAME     -------------------------------------------")
print(name)

print("-------------------------------------------     PAGE     -------------------------------------------")
print(page)

print("-------------------------------------------     IMAGE URL     -------------------------------------------")
# print(img)
print(img_url)