# Please find below attached JSON of Zomato Restaurant Page.
# Download the JSON file into your workspace, load the JSON file into your program. Once loaded we are supposed to extract the relevant data from given JSON
# https://www.zomato.com/ahmedabad/sahtain-ambli/order

import json
from rich import print

with open('Day7/Zometo.json', "r", encoding='utf-8') as f:
    data = json.load(f)
    restaurant_data = []
    days = ["monday","tuesday","wednesday","thursday","friday", "saturday", "sunday"]
    timing = data['page_data']['sections']['SECTION_BASIC_INFO']['timing']['customised_timings']['opening_hours'][0].get("timing")
    cuisines =data['page_data']['sections']['SECTION_RES_HEADER_DETAILS']['CUISINES']
    menu_path = data['page_data']['order']['menuList']['menus']
    menu_list = [menu for menu in menu_path]
    menus = []
    for menu_lst in menu_list:
       menus.append(menu_lst.get('menu'))
    print(menus)
    categories = []
    for menu in menus:
        for cat in menu.get('categories'):
            categories.append(cat)
    print(categories)
    restaurant_data.append(
        {
            "restaurant_id":data['page_info'].get("resId"),
            "restaurant_name":data['page_data']['sections']['SECTION_BASIC_INFO'].get("name"),
            "restaurant_url":data['page_info'].get("canonicalUrl"),
            "restaurant_contact":data['page_data']['sections']['SECTION_RES_CONTACT']['phoneDetails'].get("phoneStr"),
            "fssai_licence_number":data['page_data']['order']['menuList']['fssaiInfo'].get("text"),
            "address_info":{
                "full_address":data['page_data']['sections']['SECTION_RES_CONTACT'].get("address"),
                "region":data['page_data']['sections']['SECTION_RES_CONTACT'].get("country_name"),
                "city":data['page_data']['sections']['SECTION_RES_CONTACT'].get("city_name"),
                "pincode":data['page_data']['sections']['SECTION_RES_CONTACT'].get("zipcode"),
                "state":data.get("blank")
            },
            "cuisines":[
                {
                    "name": cuisine.get('name'),
                    "url": cuisine.get('url')
                } for cuisine in cuisines
            ],
            "timings":{
                day : {
                    "opening": timing.split(" ")[0],
                    "closing": timing.split(" ")[-1]
                } for day in days
            },
            "menu_categories":[
                {
                    "category_name": category.get('category').get('name'),
                    "items": [
                        {
                            "id": item.get('item').get('id'),
                            "name": item.get('item').get('name'),
                            "item_slugs": item.get('item').get('tag_slugs'),
                            "item_url": item.get('item').get('item_image_url'),
                            "item_description": item.get('item').get('desc'),
                            "item_price": float(0),
                            "is_veg": bool(item.get('item').get('dietary_slug'))
                        }
                        for item in category.get('category').get('items')
                    ]
                }
                for category in categories
            ]
        }
    )
    print(restaurant_data)

with open('Zomato_data.json', 'w', encoding='utf-8') as f:
  json.dump(restaurant_data, f, indent=4)




