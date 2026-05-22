# import os
#
# data = {"name": "Alice", "age": 30}
# json_string = json.dumps(data)
#
# print(json_string)
#
# json_string = '{"name": "Alice", "age": 30}'
# data = json.loads(json_string)
#
# print(data["name"])
#
# # Python dictionary
# data = {
#     "name": "vidhi",
#     "age": 22,
#     "city": "Ahmedabad"
# }
#
# # ---- dump (write to file) ----
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
#
# # ---- load (read from file) ----
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#
# print(loaded_data)

################################## TASK ##################################
# regex = pizza image_url 
# ^https:\/\/media-assets.swiggy.com\/swiggy\/image\/upload\/[a-zA-Z0-9\-\,\_]+\/FOOD_CATALOG\/IMAGES\/CMS\/\d{4}\/\d{1,2}\/\d{1,2}\/[a-z0-9\_\-]+.(jpg_compressed|png|jpg|jpeg)$

import json
from rich import print


with open('keyword-pizza-swiggy.json', "r", encoding='utf-8') as f:
  data = json.load(f)
  cards = data['data']['cards'][1]['groupedCard']['cardGroupMap']['DISH']['cards']
  pizzas = []
  restaurent = []
  image_url = []
  price = []
  final_price = []
  isVag = []
  ratings = []
  rating_count = []
  offers = []
  restaurent_address = []
  restaurent_locality = []
  restaurent_avg_rating = []
  restaurent_dil_time = []
  restaurent_min_dil_time = []
  restaurent_max_dil_time = []
  for i in range(1, len(cards)):
    pizzas.append(cards[i]['card']['card']['info']['name'])
    restaurent.append(cards[i]['card']['card']['restaurant']['info']['name'])
    image_url.append(cards[i]['card']['card']['info'].get('imageId', ''))
    price.append(cards[i]['card']['card']['info']['price'])
    final_price.append(cards[i]['card']['card']['info'].get('finalPrice', 0))
    isVag.append(cards[i]['card']['card']['info'].get('isVag',0))
    ratings.append(cards[i]['card']['card']['info']['ratings']['aggregatedRating'].get('rating', 0))
    rating_count.append(cards[i]['card']['card']['info']['ratings']['aggregatedRating'].get('ratingCount', 0))
    offers.append(cards[i]['card']['card']['info'].get('offerTags', [{"title": "no offer available"}])),
    restaurent_address.append(cards[i]['card']['card']['restaurant']['info']['address'])
    restaurent_locality.append(cards[i]['card']['card']['restaurant']['info'].get('locality',''))
    restaurent_avg_rating.append(cards[i]['card']['card']['restaurant']['info']['avgRating'])
    restaurent_dil_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('deliveryTime', None))
    restaurent_min_dil_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('minDeliveryTime', None))
    restaurent_max_dil_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('maxDeliveryTime', None))

restaurent_with_pizza = []

for i in range(len(pizzas)):
  restaurent_with_pizza.append({
    "restaurentName": restaurent[i],
    "itemName": pizzas[i],
    "image_url": "https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_208,h_208,c_fit/" + image_url[i],
    "price": float(price[i] / 100),
    "final_price": float(final_price[i] / 100 if final_price[i] > 0.0 else float(price[i] / 100)),
    "discount": float(float(price[i] / 100) - float(final_price[i] / 100)) if final_price[i] > 0.0 else float(0),
    "isVag": bool(isVag[i]),
    "ratings": float(ratings[i]),
    "offer": [offer.get('title', 'No offer available') for offer in offers[i]],
    "rating_count": rating_count[i],
    "restaurent_address": restaurent_address[i],
    "restuarent_url": "https://www.google.com/maps/search/?q=" + restaurent[i] + restaurent_address[i],
    "restaurent_locality": restaurent_locality[i],
    "restaurent_avg_rating": restaurent_avg_rating[i],
    "restaurent_dilivery_time": restaurent_dil_time[i],
    "restaurent_minimum_dilivery_time": restaurent_min_dil_time[i],
    "restaurent_maximum_dilivery_time": restaurent_max_dil_time[i],
  })

print(restaurent_with_pizza)

with open('swiggy_data.json', 'w', encoding='utf-8') as f:
  json.dump(restaurent_with_pizza, f, indent=4)