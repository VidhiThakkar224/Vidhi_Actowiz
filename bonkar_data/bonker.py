import json

with open ('bonker.json', "r", encoding='utf-8') as f:
    data = json.load (f)
    
    new_bonkar_data = []

    for product in data['products']:
        size = []
        for variant in product["variants"]:
            size.append(variant["name"].split('-')[1].strip())

        variants = []

        for variant in product['variants']:
            variants.append(
                {
                    "variantName": variant['name'].split('-')[1].strip(),
                    "variantId": variant['id'],
                    "variantUrl": "https://www.bonkerscorner.com/products/" + variant['name'].split("-")[1].strip() + "?variant=" + str(variant['id']),
                    "variantPrice": float(variant['price'] / 100)
                }
            )

        new_bonkar_data.append(
            {
                "product_name":product["variants"][0]["name"].split('-')[0].strip(),
                "vendor":product["vendor"],
                "product_url": "https://www.bonkerscorner.com/products/" + product["variants"][0]["name"].split('-')[0].strip().replace(" ","-"),
                "product_price":float(product["variants"][0]["price"]/100),
                "varint_count":len(product["variants"]),

                "varint_option":[
                    {
                        "optionName": "Size",
                        "optionsize":size
                    }
                ],
                 "variants":variants
            }
        )
       
    print(new_bonkar_data)
    
with open("bonker_data.json","w")as f:
    json.dump(new_bonkar_data,f,indent=4)