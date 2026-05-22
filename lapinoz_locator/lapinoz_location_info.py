import json
import requests
from lxml import html
from rich import print
import re

url = "https://lapinozpizza.in/store-locator"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

tree = html.fromstring(response.text)

result = []

# All outlet cards
outlets = tree.xpath("//div[contains(@class,'store-box')]")

print("Total outlets found:", len(outlets))

for outlet in outlets:

    outlet_name = outlet.xpath("string(.//h3)").strip()

    city = outlet.xpath(".//span[contains(@class,'city')]/text()")
    city_name = city[0].strip() if city else None

    address = outlet.xpath("string(.//p[contains(@class,'address')])").strip()

    # pincode extract
    pincode_match = re.search(r"\d{6}", address)
    pincode = pincode_match.group() if pincode_match else None

    # phone
    phone = outlet.xpath(".//a[contains(@href,'tel:')]/text()")
    phone_number = phone[0].strip() if phone else None

    # email
    email = outlet.xpath(".//a[contains(@href,'mailto:')]/text()")
    email_id = email[0].strip() if email else None

    # google map direction
    direction = outlet.xpath(".//a[contains(text(),'Direction')]/@href")
    direction_link = direction[0] if direction else None

    # opening hours
    opening_hours = outlet.xpath(
        "string(.//div[contains(@class,'timing')])"
    ).replace("\n", " ").strip()

    result.append({
        "Outlet_Name": outlet_name,
        "City": city_name,
        "Address": address,
        "Pincode": pincode,
        "Phone_Number": phone_number,
        "Email": email_id,
        "Opening_Hours": opening_hours,
        "Direction_Link": direction_link
    })

print(result)

# save json
with open("lapinoz_all_outlets.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("\nData saved successfully")