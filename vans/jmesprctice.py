import json
import jmespath
from rich import print

with open(r'C:\Python Training\Day7\Zomato.json', "r", encoding='utf-8') as f:
    data = json.load(f)

query = "page_info"

result = jmespath.search(query, data)

print(result)