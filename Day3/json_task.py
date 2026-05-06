import json
from rich import print

with open('keyword-pizza-swiggy.json','r',encoding='utf-8')as file:
    data = json.load(file)
cards = data['data']['cards'][1]['groupedCard']['cardGroupMap']['DISH']['cards']

pizza = []
restaurent = []
img_url = []
price = []
final_price = []
isveg = []
rating = []
rating_count = []
offer = []
address = []
locality = []
avg_rating = []
delivery_time = []
min = []
max = []

for i in range(1, len(cards)):
    pizza.append(cards[i]['card']['card']['info']['name'])
    restaurent.append(cards[i]['card']['card']['restaurant']['info']['name'])
    img_url.append(cards[i]['card']['card']['info'].get('imageId', ''))
    price.append(cards[i]['card']['card']['info']['price'])
    final_price.append(cards[i]['card']['card']['info'].get('finalPrice', 0))
    isveg.append(cards[i]['card']['card']['info'].get('isVag',0))
    rating.append(cards[i]['card']['card']['info']['ratings']['aggregatedRating'].get('rating', 0))
    rating_count.append(cards[i]['card']['card']['info']['ratings']['aggregatedRating'].get('ratingCount', 0))
    offer.append(cards[i]['card']['card']['info'].get('offerTags', [{"title": "no offer available"}])),
    address.append(cards[i]['card']['card']['restaurant']['info']['address'])
    locality.append(cards[i]['card']['card']['restaurant']['info'].get('locality',''))
    avg_rating.append(cards[i]['card']['card']['restaurant']['info']['avgRating'])
    delivery_time.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('deliveryTime', None))
    min.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('minDeliveryTime', None))
    max.append(cards[i]['card']['card']['restaurant']['info']['sla'].get('maxDeliveryTime', None))

restaurent_with_pizza = []

for i in range(len(pizza)):
  restaurent_with_pizza.append({
    "restaurentName": restaurent[i],
    "itemName": pizza[i],
    "image_url": "https://media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_208,h_208,c_fit/" + img_url[i],
    "price": float(price[i] / 100),
    "final_price": float(final_price[i] / 100 if final_price[i] > 0.0 else float(price[i] / 100)),
    "discount": float(float(price[i] / 100) - float(final_price[i] / 100)) if final_price[i] > 0.0 else float(0),
    "isVag": bool(final_price[i]),
    "ratings": float(rating[i]),
    "offer": [offer.get('title', 'No offer available') for offer in offer[i]],
    "rating_count": rating_count[i],
    "restaurent_address": address[i],
    "restuarent_url": "https://www.swiggy.com/city/ahmedabad/?q=" + restaurent[i] + address[i],
    "restaurent_locality": locality[i],
    "restaurent_avg_rating": avg_rating[i],
    "restaurent_dilivery_time": delivery_time[i],
    "restaurent_minimum_dilivery_time": min[i],
    "restaurent_maximum_dilivery_time": max[i],
  })

print(restaurent_with_pizza)

with open('swiggy_data.json', 'w', encoding='utf-8') as f:
  json.dump(restaurent_with_pizza, f, indent=4)