from curl_cffi import requests
from parsel import Selector
import json, jmespath
from datetime import datetime

final_data=[]
def process(url):

    url = url

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'aka_locale=en-in; MUID=459A6298FD1A47A9BAA25BF9CA369F37; MSCC=NR; 3PAdsOptOut=0; _fbp=fb.1.1780632815961.249424268995345930; MSFPC=GUID=f204b4a26785210d75048b1a0d6adb55&HASH=f204&LV=202604&V=4&LU=1777291823334; TiPMix=14.496516313535102; x-ms-routing-name=self; x-theme=Dark; x-theme=Dark; ai_session=OPeSsuIQcc1v/6i8b0nN7H|1780655318896|1780656878908',
}

    html = requests.get(url, headers=headers).text
    selector = Selector(html)
    script = next((s for s in selector.xpath("//script/text()").getall() if "__PRELOADED_STATE__" in s),None)

    json_str = extract_json(script)

    data = json.loads(json_str)

    with open("latestdata.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    products = jmespath.search(
    "core2.products.productSummaries.*",data)[0]

    multiplayer_choices = jmespath.search(
        "core2.filters.Browse.data.Multiplayer.choices[].title",
        data
    )

    product = {
        "game_name": jmespath.search('title', products),

        "game_url": url,

        "rating": jmespath.search('averageRating', products),

        "thumbnail_url": jmespath.search(
            'images.poster.url',
            products
        ),

        "game_description": jmespath.search(
            'description',
            products
        ),

        "publisher_name": jmespath.search(
            'publisherName',
            products
        ),

        "game_images": jmespath.search(
            'images.screenshots[].url',products
        ),

        "published_date": jmespath.search(
            'releaseDate',
            products
        ),

        "developer_name": jmespath.search(
            'developerName',
            products
        ),

        "genre": jmespath.search(
            'categories',
            products
        ),

        "capabilities": jmespath.search('capabilities',products),

        "available_on": jmespath.search(
            'availableOn',
            products
        ),

        "offers": jmespath.search(
            'specificPrices.purchaseable[*].listPrice',
            products
        ),

        "system_requirements": jmespath.search(
            'systemRequirements',
            products
        ),

        "content_rating": jmespath.search(
            'contentRating.rating',
            products
        ),

        "feature_list": jmespath.search(
            'contentRating.descriptors',
            products
        )
    }

    if product.get("published_date"):

        date_str = product["published_date"][:26] + "Z"

        product["published_date"] = datetime.strptime(
            date_str,
            "%Y-%m-%dT%H:%M:%S.%fZ"
        ).strftime("%d-%m-%y")

    final_data.append(product)

def extract_json(text):
    start = text.find("{")
    if start == -1:
        return None

    brace = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            brace += 1
        elif text[i] == "}":
            brace -= 1

        if brace == 0:
            return text[start:i+1]

    return None


with open("titles.json", "r", encoding="utf-8") as f:
    data=json.load(f)

for item in data:
    url = item.get('url')
    print(url)
    process(url)

with open("latest.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4, ensure_ascii=False)