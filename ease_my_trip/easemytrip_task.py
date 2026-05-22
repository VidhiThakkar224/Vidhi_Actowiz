import json
import jmespath
from rich import print

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

with open(r"C:\Python Training\Day10\easemytrip.json", "r", encoding="utf-8") as f:
    data = json.load(f)

flights = data.get("dctFltDtl")

flight_list = list(flights.values())

total_stops = f"{jmespath.search('STP', flight_list[0])}-Stop"

fare_data = jmespath.search("j[0].s[0]", data)

sid = jmespath.search("SID", fare_data)

flight_details = []

for v in flight_list:

    departure_code = jmespath.search("OG", v)

    arrival_code = jmespath.search("DT", v)

    flight_info = {

        "flight_id": (
            f"{jmespath.search('AC', v)}"
            f"{jmespath.search('FN', v).strip()}"
        ),

        "flight_name": jmespath.search("FlightName", v),

        "day": "Monday",

        "date": (
            jmespath.search("DDT", v)
            .replace("Mon-", "")
        ),

        "departure_city": airport_map.get(
            departure_code,
            departure_code
        ),

        "departure_time": jmespath.search("DTM", v),

        "departure_terminal": (
            f"Terminal - {jmespath.search('DTER', v)}"
        ),

        "arrival_city": airport_map.get(
            arrival_code,
            arrival_code
        ),

        "arrival_time": jmespath.search("ATM", v),

        "arrival_temrinal": (

            f"Terminal - {jmespath.search('ATER', v)}"

            if jmespath.search("ATER", v)

            else "No Terminal Data Given"
        ),

        "time_duration": (
            jmespath.search("DUR", v)
            .replace("h ", ":")
            .replace("m", ":00")
        ),

        "flight_class": jmespath.search("CB", v)
    }

    flight_details.append(flight_info)

flight_information = {

    "total_base_far": int(
        float(
            sid.split("TBA=")[1].split(",")[0]
        )
    ),

    "tax": int(
        sid.split("Tax=")[1].split(",")[0]
    ),

    "total": int(
        float(
            sid.split("TFA=")[1].split(",")[0]
        )
    )
}

final_output = {

    "total_stops": total_stops,

    "flight_details": flight_details,

    "flight_information": flight_information
}

print(final_output)