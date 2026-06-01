from rich import print
import json
from curl_cffi import requests
import jmespath

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.nseindia.com/market-data/live-market-indices',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'AKA_A2=A; _ga=GA1.1.677588674.1780289116; ak_bmsc=62FD2E74716ECA877001DA9651ED3DCE~000000000000000000000000000000~YAAQz68nF+a1r0GeAQAALgGAgQCiLIvb+Hi0ZTM0As+fFrNvcASvoMtmoAs7pwng6SoW/MbwI2J8hI/4b0w9sGT9F/eJkm7e2TYmwBtlOxhNDQok5t8kKqcYreP5qOWl9JAP9BCTCqdukHupCAdGIzACMKWGfzQ1GzynDnRWEThCKqBdXMNGNkLCEvDv0k5pIFkVtQZMbK5brOOJhyBfDFtoFkMjB+2/J7bAHNIVSWsyqTNzRYijHzw+eY5pH/Vwk3IdZrqQUluipt7r8YLeVOveZ0b0mKoHdG4ynMTqu4xaIr4UCDEBxPd/RyOQBwXS9OvvOYBDs3IjALUBsN92UqMkX7imdTD/YVqzLHn1NiWMf6HVpHHjPrOGHfqHXknh6iQGlUOmiZwq0m0D+TNijlYmi9nwkWU0jkqbnZKA64JGQ8mGRH3H8a2J5e3H/xi2fdQtIsNTM+5GaNReTHGS920=; nsit=bFLgCxuhTCrI-zamL_8b4AJp; bm_sz=460C253963D39755F7F018A8D0D98037~YAAQz68nFyiIsEGeAQAArjuDgQDt+onV0zIPn56kGIjxMVoqwe+xnTOkDe0XaRzScN4bzpjsQ60dzti4WgsgvDb+UM/AkBmb+I9lm0hUXMySaw+v7gLhMkqXezxI30brSsLAAGEXdBqp85YwDachReZpaxtSLJeN5fnV4EfVvJ5wH7wBCSrRIgw3fUW2v/XQDpUBA0rIx70FeTIXTq7AtfZBBAqcjlB70xr0QfbkwMyxDlX8UGAbmiAtBcsuSeBOmE/wWIdPfpxZCDIR5rpE0W50MvmQdmha9T2CmVtgztjeNky+IbAva3b9oZPat8YiIOQU5JQNfqkkYlpU8zXSw85yk04L944kWbw8Mj0HWpHCJGjXobn8sxY8Ekv+Xiq2hI27zv+/TFAAGwoVN14vap5PGnPuwDlk3eVz3Nlfs9e81G0=~4408130~3552052; _abck=FE3E5A64D250EFFF357440C4474AF7D1~0~YAAQz68nF46IsEGeAQAA0D2DgQ8Dyly6SN28GL7pF2/S5S71mVxSkM5QreqvFlJdKlCaKPVotH8D62jdDw2kILknBUBxSxna/qToiYnT/T32RJrX/4vA3S1Hcg5KeJuaZz4P+N3maGl4hnGWXOaLH9d5wVIen6b6jloTCivfJAfNes8E1EkJnf7N0z11+iiqZ1Es/YC0qVZCvFFM8BgvUMDU33y7tArCjq+jrwTzMJw1N24F4oT5KGfanXArSQRbHeRz3nBqw0nfdl70KN9quBR008Tu3sf3rVAxA/N0/Ameh7gENRP8cGm02WxGRyEbJ3floNbLCeFO8p5nNQS16VVjiHqRMFqG4gERSIS3EEmMoiI+7IW47eDyjjlbvAxoxWlJNWa60g8Vn3K957JHvyFtluNzO5nk4sr5Mtt4ekwg2rNC4ReZi0uQTiY8hkEa353uFG45XI8nX/gJxHEf6mStgMWOrX0nv6Huzkr/As82dag4ODIWHE8XeJ75SGT+9u/oj1YeCKhspE9Vw7z60AfyCxR0xHLW/o4b+MonqzQSZzgns8X3yAhHJXfW4ZWR+uX7mzuRXgLYBC+9/bfNxbSjFgtVhvD3/3Fb5G0+sIRavsKMBPTcpAKTsaMCyCK0QIcPaFY9EyxM2Jg=~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f+4J1PhskJmkcfrS4eC3Sjdlf8sO94IEKasJITDI%2fSiuo7Nr2lNL2u2ctdppNIaq6lwIyjYFUz9WtdmD+%2f0CJTTXa%2fdAuNY1iNQx~-1; RT="z=1&dm=nseindia.com&si=5a761881-04b7-4548-a186-17096a6dfb7f&ss=mpuq68no&sl=1&se=8c&tt=145&bcn=%2F%2F684d0d47.akstat.io%2F"; _ga_87M7PJ3R97=GS2.1.s1780289115$o1$g1$t1780289329$j59$l0$h0; bm_sv=1D2CB3DEE4154AC1A2CE7747594E4A2A~YAAQz68nF9iJsEGeAQAAOEKDgQD0r5Ck1sYaJBmbXUcmkBnTDFims3VTsQ8rQNH4Z5Ro5D6asrSLmTnhNC0oB1XKNkpKc/z1bNsL544MEUF3yipzX6N9NXCppFddDJxTUmVPvIZTzfsSV579PlI96K+h9j8Q2Y6IELL1W3FeBjzh3Z9MvABmQhRsMAGyeuNrDRRc897JLoSYqcK4yBnw0roJyBUZEwV4dYIOYpzikUmcOFe5zbbBUfY/HqPRifMHa+sR~1',
}

response = requests.get('https://www.nseindia.com/api/allIndices',headers=headers)

all_data = response.json()

with open(r"C:\Python Training\nse_india\all_indicies_data.json","w",encoding='utf-8') as f:
    json.dump(all_data,f,indent=4,ensure_ascii=False)

result=[]

sectorals=jmespath.search("data[?key=='SECTORAL INDICES']",all_data)

for sectoral in sectorals:
    index_symbol=jmespath.search("indexSymbol",sectoral)
    index_name=index_symbol.replace(" ","%20")

    api_url=f"https://www.nseindia.com/api/equity-stock-indices?index={index_name}"
    api_response=requests.get(api_url,headers=headers,impersonate="chrome120")
    # print(api_url)
    data=api_response.json()
    # print(data)
    
    result.append({
            "sectoral_indices":jmespath.search("index",sectoral),
            "sectoral_data":[{
            "symbol":jmespath.search("symbol",d),
            "open":jmespath.search("open",d),
            "dayHigh":jmespath.search("dayHigh",d),
            "dayLow":jmespath.search("dayLow",d),
            "previousClose":jmespath.search("previousClose",d),
            "ltp":jmespath.search("lastPrice",d),
            "change":jmespath.search("change",d),
            "change_percentage":jmespath.search("pChange",d),
            "volume(shares)":jmespath.search("totalTradedVolume",d),
            "value(crores)":jmespath.search("totalTradedValue",d),
            "52W H(year high)":jmespath.search("yearHigh",d),
            "52W L(yearLow)":jmespath.search("yearLow",d),
            "percentage_Change_30days":jmespath.search("perChange30d",d),
            "date":jmespath.search("lastUpdateTime",d)
            }for d in jmespath.search("data", data)]
        })
print(result)
print(len(result))

with open (r"C:\Python Training\nse_india\sectoral_indices_stock_data.json",'w',encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False) 


# #SECTORAL INDICIES NAME
# import json
# import jmespath
# from rich import print
# from curl_cffi import requests
# from urllib.parse import quote

# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'no-cache',
#     'pragma': 'no-cache',
#     'priority': 'u=1, i',
#     'referer': 'https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20FINANCIAL%20SERVICES%2025%2F50',
#     'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
#     # 'cookie': '_ga=GA1.1.718645797.1780288726; ak_bmsc=D6C59C71EDE7D4B79AF0CF7C78D811EF~000000000000000000000000000000~YAAQyq8nF5sNmUOeAQAAQiR6gQAljF83gtrCkToVmvblnz2FJQZHCw2sbtmsQ41cbTWRLQ5OeUs2s23s64S/owwyUzZftbnlDsNXyZ7nn1LraS1OUURpZDHnqL9GpSuH1Kb1HY/MpjF0QzsWHOwe9c/h6iAVjFpAD7thSTtPHnltjxL475u99NN3kRewFIyITrnG8yXqVwpqNnQR0AtPcjW02tFTPpBSQNBHjta+d6A0sfMprhIt7os+65HsGbNTp8wtUbHAGzXkzuDHT0ieYOmLYlUe/hdkul10YpW8bnZPqRUydY9Lngt4EIlj0UHH+eCH9VHS9O1TMN3QgqJ+z9C5Z0FTUw54xvej1Dhnm/QpzpbgmvZza3oK6bWRNkmMVMENo+g8tzjCwyCRwPwJe4UpVlWwvus7W3Z+4v79GHMvtDlRrqEHLSV5g3jlzoIwXlzEd2hG9/LAhrz4Wy7ym58=; nsit=lOOT4JBIRY6prPsyZY0iEFPD; browse-url=%2Fget-quote%2Fequity%2FAUTOBEES%2FNippon-India-Mutual-Fund---Nippon-India-Nifty-Auto-ETF; _ga_87M7PJ3R97=GS2.1.s1780288725$o1$g1$t1780292249$j59$l0$h0; _abck=29A1BE22749412F53EC8D8752D0A1BAB~0~YAAQyq8nF38zokOeAQAATA6wgQ85xd+20NJ0UPidRHxuGF1zCeYE5m9016zOWiioGeLgUroo8edvkNQyatFBt1VYDqd1gI8ztETvWUsrYfGs0V34VlqYzIHDogYBhIdsUtQCKVJDlPx+5g+lJVL0P1PlUEHS9eRcGVGcKDnSqyr5OVOsIYBlB+lzZ/cOwJddmt5J7PO4viJZzuwpMvQyFQ15fYI8ffOWqW+eGlyBt2ydCxNZzT0RnBuEVqucaBL6J0fLCSN/8TwxCJeXHv4+DJOIJ1vHpgxEO42ETlR/wxZ44r8YqZ4yPq5yapFlZjux+QP4VHCy6pSdOc7kkT3AOUlZCPp32or6sqYhC+lsF2zcmtDYblSv5woJYVYaBtPewlWPui3Pu2+aMgLdoEtPtuswK8CyVPpGmfgsxAV3qcLBNAqxUqdB0mOzo5tZDiE8NRtACmZNUOrJmIPlD5x483iEdAHh5TnawGOkGwVvSiKP6b6E+6IncwVGPC3n2ev+S+KHMX4c//ut0JxuVS0MU5nuY9++9G1CWOWcNSJGos9uHhG1RJLi/HjpXa0pDKq/dipUKCCDfHwHvnUWcc75plTULpMbEgTg8ZjBOvr2b4kMzECA2LoLqjMY+UAICPF2BbQeyLn34hNiczGKBaN2Et3+oL4dg4KoAcfbnv4Ojc+NXiEpul/oasypOwGiBA+wUVqVs5ZV4Zauej86Ax7R7xtlJ3Tsfw==~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f2eR8BQUZk7gAbmS%2f08PKGQBmzpOp0gyMESqKJzjtptSetxsOAz+RZAH6PVTiYaq11Xh4OvA%2fqaTCSxrXbWJ5xQr9S0dAWSjhhINSQsDdj5sNjDGeyZ9Qv%2fGhnI4+p4FCDPlgHg46CoPqRxyI08WzpIaMLQMouGuL7swRPxe8w%3d%3d~-1; AKA_A2=A; bm_sz=FC05382DB83763E279AF1EC7E3940AA6~YAAQyq8nF/ORokOeAQAAjWOzgQA7szWeEtr2MmgDhkNAgvoeJgrzosae1f2Wu5Qx/GvS0BF+lHUYUncnc3OvfhXNgMVysBcSd8GkVLeSlsHMYKqB3qk4H5z26TZBiRTRfzUnQ1oyAJtYqiAiQTkvj0BqSgBgJWLmwpR/JjBNVUrzDvHaRa+kUTVcGDEWDkt/nmKuyeXhdk1rxCJkeKLl8AjmMcXO4SnTXcCXmhiZnwsFTPzwxmZVTYEQvVTXkjrpzOqMCG/pSzUdg+AghJ6NcVMcEbgncKs6xKxxOsjdGsdLBrnNmOH6rBb5O64tuVzBEFgQGAdW4wbfflpuONQSnBLDCEf84W3LgNQPBHpq+gRpfx4fHEm8SRDkMlEOwW/I/pGKv2nNx9nHuCYaNnbPImEHormgbdd3jxEBLkPj5Nlu13pPLxiIaUWeOzpgRmPllD1FY47czapakIdTZmnJI5c+LMbhYd6micQeMFe6dREMNdkDvLq+wPveISYv5kwrZMhU96KlIkZTJlPJK0nfuJQuTE6MKbhBEqqf+fgVikuL4GLY9dA=~3294004~4277826; RT="z=1&dm=nseindia.com&si=11cb0919-07aa-4685-9585-142deb4d8c64&ss=mpus1dgi&sl=0&se=8c&tt=0&bcn=%2F%2F684d0d46.akstat.io%2F"; bm_sv=0863DDA3D8F6668D7BAB366233B9A829~YAAQyq8nFxfAokOeAQAA7gm1gQDrYUtJj5/FUg2bzyvKVusQ6+6ZJhQL+LWnEbHhAvHyfEIpsXPs71Ou6JlR82TQ0C3ohvliJ/DNblWKvo2YV1gsBYtpGTRAeeu+jkG24WY4LBvIpXK4UmIoewsYA7rPK6Lyd5/bmaqUbmCwjaixvPYB1BJba9t4mIBRv0QGzj+frafYakO5AW+pcZtRNNfd5T8hxNWVt8YFiOGWjXIglp/bE/YGeluiLlmR3TQ6fkzsWQ==~1',
# }

# with open (r"C:\Python Training\nse_india\all_indicies_data.json","r",encoding='utf-8')as f:
#     data = json.load(f)

# indicies = []
# info = jmespath.search("data[?key=='SECTORAL INDICES'].index[]", data)

# for index_name in info:
#     print(index_name)

#     api_url = f"https://www.nseindia.com/api/equity-stock-indices?index={index_name}"

#     response = requests.get(
#         api_url,
#         headers=headers,
#         impersonate="chrome120"
#     )

# all_stocks = []

# INDEX_MAPPING = {
#        "NIFTY AUTO",
#         "NIFTY CEMENT",
#         "NIFTY CHEMICALS",
#         "NIFTY CONSUMER DURABLES",
#         "NIFTY FINANCIAL SERVICES EX-BANK",
#         "NIFTY FINANCIAL SERVICES 25/50",
#         "NIFTY FMCG",
#         "NIFTY HEALTHCARE INDEX",
#         "NIFTY IT",
#         "NIFTY MEDIA",
#         "NIFTY METAL",
#         "NIFTY MIDSMALL HEALTHCARE",
#         "NIFTY MIDSMALL FINANCIAL SERVICES",
#         "NIFTY MIDSMALL IT & TELECOM",
#         "NIFTY OIL & GAS",
#         "NIFTY PHARMA",
#         "NIFTY PSU BANK",
#         "NIFTY PRIVATE BANK",
#         "NIFTY REALTY",
#         "NIFTY REITS & REALTY",
#         "NIFTY500 HEALTHCARE"
# }

# for index_name in info:

#     api_index = INDEX_MAPPING.get(index_name, index_name)

#     api_url = (
#         "https://www.nseindia.com/api/equity-stock-indices?index="
#         + quote(api_index)
#     )

#     response = requests.get(
#         api_url,
#         headers=headers,
#         impersonate="chrome120"
#     )

#     json_data = response.json()

#     if not json_data:
#         print(f"Skipping : {index_name}")
#         continue

#     trade_date = jmespath.search("timestamp", json_data)
#     stocks = jmespath.search("data[*]", json_data)

#     if not stocks:
#         print(f"Data not found : {index_name}")
#         continue

#     for stock in stocks:

#         all_stocks.append({
#             "index_name": index_name,
#             "date": trade_date,
#             "symbol": jmespath.search("symbol", stock),
#             "open": jmespath.search("open", stock),
#             "high": jmespath.search("dayHigh", stock),
#             "low": jmespath.search("dayLow", stock),
#             "previous_close": jmespath.search("previousClose", stock),
#             "last_price": jmespath.search("lastPrice", stock),
#             "change": jmespath.search("change", stock),
#             "pchange": jmespath.search("pChange", stock)
#         })
        
# with open("sectoral_indices_stock_data.json","w",encoding="utf-8") as f:
#     json.dump(all_stocks, f, indent=4, ensure_ascii=False)