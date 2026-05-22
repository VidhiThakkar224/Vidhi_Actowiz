import json
from lxml import html
from rich import print

with open(r'C:\Python Training\Day12\hrrisfarm.html', "r", encoding='utf-8') as f:
    data = f.read()
    result = []

    tree = html.fromstring(data) #use html file parse

    result = tree.xpath("//div[text()='Shop Categories']/following-sibling::li/a")

    base_url = "https://www.harrisfarm.com.au"

    categories = []

    for i in result:
        name = i.text_content().strip()
        link = i.get("href")
        full_link = base_url + link

        category_data = {
            "category_name": name,
            "category_link": full_link
        }
        categories.append(category_data)

for category in categories:
    print(category)

with open('harrisfarm_data.json', 'w', encoding='utf-8') as f:
  json.dump(categories, f, indent=4)