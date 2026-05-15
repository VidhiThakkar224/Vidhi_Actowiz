import json
import jmespath
from datetime import datetime
import re

from pydantic import BaseModel, Field
from typing import List

with open("C:\\Python Training\\Day10\\easemytrip.json", "r", encoding="utf-8") as f:
    data = json.load(f)

d=open(r"C:\\Python Training\\Day10\\easemytrip.json").read()
data1 = json.loads(d)

class Flight(BaseModel):

    source: str
    destination: str
    date: str
    departure: str
    arrival: str
    departure_terminal : str
    arrival_terminal : str
    durationtime: str
    airline: str
    cl:str

    flight_no: str = Field(
        min_length=4,
        max_length=8
    )

class FlightGroup(BaseModel):

    data: List[Flight]

    base_price: float = Field(gt=0)

    tax_price: float = Field(gt=0)

    final_price: float = Field(gt=0)

profile = """
j[0].s[*].{
    eid: EID,
    data: segMatchingKey,
    flight : FN
}"""

bp = jmespath.search("j[0].s[*].AP", data)
tp = jmespath.search("j[0].s[*].APT", data)
total = jmespath.search("j[0].s[*].PT", data)
profile_data = jmespath.search(profile, data)
cl = jmespath.search("j[0].s[*].lstFr[0].CB",data)
fl = jmespath.search("j[0].s[*].b[*].FL",data)
newdterlist = []

finalfl =[]
for eachfl in fl:
          finalfl.extend(eachfl)
# print(len(finalfl))
airport_map = {

    "DEL": "New Delhi",
    "JAI": "Jaipur",
    "NMI": "Navi Mumbai",
    "BHO": "Bhopal",
    "HDO": "Ghaziabad",
    "AMD": "Ahmedabad",
    "BOM": "Mumbai",
    "HSR": "Hirasar",
    "LKO": "Lucknow",
    "VNS": "Varanasi",
    "HYD": "Hyderabad",
    "IXD": "Prayagraj",
    "IDR": "Indore",
    "RPR": "Raipur",
    "NAG": "Nagpur",
    "BDQ": "Vadodara",
    "GOI": "Goa",
    "DED": "Dehra Dun",
    "IXC": "Chandigarh",
    "UDR": "Udaipur",
    "ATQ": "Amritsar",
    "BLR": "Bengaluru",
    "PAT": "Patna",
    "SXR": "Srinagar",
    "DBR": "Darbhanga",
    "GOX": "Goa",
    "IXR": "Ranchi",
    "BBI": "Bhubaneswar",
    "IXB": "Bagdogra"
}

flight_map = {

    "6E": "IndiGo",
    "AI": "Air India",
    "QP": "Akasa Air",
    "SG": "SpiceJet",
    "IX": "Air India Express"
}

pattern = r"([A-Z]{3})([A-Z]{3})([A-Za-z]{3}-\d{2}[A-Za-z]{3}\d{4})(\d{2}:\d{2})(\d{2}:\d{2})([A-Z0-9]{4,8})"

all_flights = []

i = 0

for idx, item in enumerate(profile_data):

    value = item.get("data")

    if not value:
        continue

    flights = value.split("^")

    flights_list = []

    for index,flight_data in enumerate(flights):
        departure_termimal = jmespath.search(f'dctFltDtl."{finalfl[idx][index]}".DTER', data1)
        arrival_temrinal = jmespath.search(f'dctFltDtl."{finalfl[idx][index]}".ATER', data1)

        match = re.search(pattern, flight_data)

        if match:

            flight_number = match.group(6)

            airline_code = flight_number[:2]
            deptime = datetime.strptime(match.group(4),"%H:%M")
            arrtime = datetime.strptime(match.group(5),"%H:%M")

            flight_dict = {

                "source": airport_map.get(match.group(1),match.group(1)),

                "destination": airport_map.get(match.group(2),match.group(2)),

                "date": datetime.strptime(match.group(3),"%a-%d%b%Y").strftime("%d-%m-%Y"),

                "departure": match.group(4),

                "durationtime" : str((arrtime - deptime)),

                "arrival": match.group(5),

                "departure_terminal": "no terminal data found" if not departure_termimal else "Terminal - " + departure_termimal,
                "arrival_terminal": "no temrinal data found" if not arrival_temrinal else 'Terminal - ' + arrival_temrinal,

                "flight_no": flight_number,

                "airline": flight_map.get(airline_code,"Unknown Airline"),

                "cl" :cl[i]
            }

            validated_flight = Flight(**flight_dict)

            flights_list.append(validated_flight.model_dump())

    group_dict = {

        "data": flights_list,

        "base_price": bp[i],

        "tax_price": tp[i],

        "final_price": total[i]
    }

    try:

        validated_group = FlightGroup(**group_dict)

        all_flights.append(
            validated_group.model_dump()
        )

    except Exception as e:

        print(e)

    i += 1

with open("EasemytripData.json", "w", encoding="utf-8") as f:

    json.dump(all_flights,f,indent=4,ensure_ascii=False)

print("Json Data")