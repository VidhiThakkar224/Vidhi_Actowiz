from rich import print
import json
from curl_cffi import requests
from lxml import html
import jmespath
from urllib.parse import quote

url = "https://www.xbox.com/en-IN/games/browse?Genre=Strategy"

with open(r"C:\Python Training\Xbox_games\stratey_data.json","r",encoding="utf-8") as f:
    data = json.load(f)

# encodedCT = "eyJIYXNNb3JlIjp0cnVlLCJTa2lwQ291bnQiOjI2LCJUb3RhbENvdW50IjoyNjg0LCJQcmV2aW91c1BhZ2VQcm9kdWN0SWRzIjpbIkJUNVAyWDk5OVZIMiIsIkJRMVROMVQ3OVY5SyIsIkJYQkpRMTkzMjEzOCIsIjlNVFJIMkg3NVpTNCIsIjlOTDFUUFRNNVIxVCIsIjlQNlFOQzJRM1Y5ViIsIjlOSlA0QlFQSFhCQiIsIjlQNkxOTjNLWjc1UiIsIjlQRFhRRkc1VEZKMCIsIjlOMjAxNzNXR0IzMyIsIjlQQzFEQ0I0MjlHUiIsIjlQM0dMWEpEWlQ0OSIsIkMwOEpYTkswVkc1TCIsIjlQMkoxWFMxWDI1USIsIjlOSDI4MVZGUzdUSiIsIjlOS0NLRDFXTkRRMCIsIjlORDU4TFFURzA5VCIsIjlQNFpYTkZYMjExSCIsIjlQSjlLMlBKNTFWRyIsIjlQRjZKSjVRMzBHVyIsIjlQSjNCMzVSTjk0VyIsIjlQN0ROUVJGTFI1VCIsIjlOOEJWOVNOSzc1RyIsIjlOTFZXTDhHMlAxSCIsIjlQMEJHV0NONzJWUCJdfQ=="

result = []

# while True:
#     payload = {
#         "encoded_CT":encodedCT
#     }

#     response = requests.post(url,json=payload).json()

#     products = response["products"]
#     result.extend(products)

#     encodedCT = response.get("encoded_CT")

#     if not encodedCT:
#         break
    
games = list(data["core2"]["products"]["productSummaries"].keys())

for game_id in games:

    game = data["core2"]["products"]["productSummaries"].get(game_id)
    if not game:
        continue

    game_name = jmespath.search('title', game) or ""

    safe_name = quote(game_name.replace(" ", "-"))

    result.append({
        "game_name": game_name,
        "game_url": f"https://www.xbox.com/en-IN/games/store/{safe_name}/{game_id}/0001",
        "game_description": jmespath.search('description', game),
        "game_images": jmespath.search('images.boxArt.url', game),
        "published_date": jmespath.search('releaseDate', game),
        "genre": jmespath.search('categories', game),
        "offers": jmespath.search('specificPrices.purchaseable[0].listPrice', game),
        "operating_system": jmespath.search('availableOn', game),
        "content_rating": jmespath.search('contentRating.ratingDescription', game),
        "feature_list": jmespath.search('features', game),
    })

print(result)
print("TOTAL:", len(result))