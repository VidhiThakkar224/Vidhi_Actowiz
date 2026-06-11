from curl_cffi import requests
from lxml import html
import pymongo
import os
from rich import print
import time
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

start_time = time.time()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient["only_db"]
collection = my_db["product_urls"]

product_urls = [doc["product_url"] for doc in collection.find()]

print(f"Total URLs in DB: {len(product_urls)}")

product_urls = product_urls[start:end]

print(f"Processing URLs: {start} -> {end}")
print(f"Current Batch: {len(product_urls)} URLs")

print(f"Total URLs: {len(product_urls)}")

for url in product_urls:
    try:
        resp = requests.get(url, impersonate="chrome120", timeout=30)
        tree = html.fromstring(resp.text)

        image_urls = tree.xpath('//img/@src | //img/@data-src')

        slug = url.rstrip("/").split("/")[-1]
        slug_id = slug.split("-")[0]

        image_urls = [img for img in image_urls if f"{slug_id}_g" in img]
        image_urls = list(dict.fromkeys(image_urls))
        image_urls = sorted(image_urls)

        if not image_urls:
            print(f"No images found: {url}")
            continue

        folder_path = os.path.join(r"C:\python training\only", "product_images", slug)
        os.makedirs(folder_path, exist_ok=True)

        for image_url in image_urls:
            if image_url.startswith("//"):
                image_url = "https:" + image_url
            if not image_url.startswith("http"):
                continue

            try:
                img_resp = requests.get(image_url, impersonate="chrome120", timeout=15)
                image_name = image_url.split("/")[-1].split("?")[0]
                image_file = os.path.join(folder_path, image_name)

                with open(image_file, "wb") as f:
                    f.write(img_resp.content)

                print(f"Saved: {image_file}")

            except Exception as e:
                print(f"Image error {image_url}: {e}")

    except Exception as e:
        print(f"Error {url}: {e}")

end_time = time.time()

print(f"\nExecution Time: {end_time - start_time:.2f} seconds")
print(f"\nExecution Time: {(end_time - start_time)/60:.2f} minutes")

print("Done!")