from curl_cffi import requests
from parsel import Selector
import json
import jmespath
import re

titles = []
base_url = 'https://www.xbox.com/en-IN/games/store/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'aka_locale=en-in; MUID=A8E1E45231DF431CA23A78A2154B753A; MSCC=NR; 3PAdsOptOut=0; _fbp=fb.1.1780632322565.16117727650999083; MSFPC=GUID=70d88ee140e6401a99778e2a1b0e0c8f&HASH=70d8&LV=202604&V=4&LU=1777452775837; x-theme=Light; TiPMix=88.39593053534426; x-ms-routing-name=self; x-theme=Light; ai_session=aRgvSLHYyAhIdfRE0jCrE7|1780644658766|1780650983952',
}

params = {
    'Genre': 'Strategy',
}


def slugify(text: str) -> str:
    text = text.lower().strip()

    # remove special symbols
    text = re.sub(r"[™®©']", "", text)

    # replace non-alphanumeric with space
    text = re.sub(r"[^a-z0-9\s-]", " ", text)

    # spaces → hyphen
    text = re.sub(r"\s+", "-", text)

    # collapse multiple hyphens
    text = re.sub(r"-+", "-", text)

    return text.strip("-")

def getdataFromApi(encodeCT):
        # print(encodeCT)
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'ms-cv': 'gSiRfkhJV73vjtjXck98jv.19',
            'origin': 'https://www.xbox.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.xbox.com/',
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
            'x-ms-api-version': '1.1',
            'xbl-experiments': 'enableuhfcache,forcerefreshexp,forceservernav,enableaamscript,enableserversideuserfeatureassignments,enableserverauthv3,aatest9010,aatestdevice9010,aatest_50_50,aa_post_v3_2_1_5050,aa_test_device_50_50,autofullscreenpersist,disablexgp,enableaapaddfriendstream,enableaapmultiplayertitle,enableaapscreentimestream,enableabsolutemouse,enableaccountlinking,enableachievements,enableageverificationstatus,enableaionageverification,enableaionageverificationactions,enableanontelemetry,enableaskaparentaddfriend,enableaskaparentcontent,enableaskaparentscreentime,enableauthv2ew,enableauthv2ewtizen,enablebundlebuilderadobelaunch,enablebuynowdynamicmeparams,enablebuynowxboxuiexp,enablebyog,enablebyogpurchase,enablecanton,enablecardbadgeedgewater,enablecartcheckoutdynamicparams,enablecartmoraystyling,enablecelestiaxboxcom,enablechangegamertag,enablechatimageupload,enableclientauthv3,enableclientguide,enableclientguideinstream,enableclientrenderedcursor,enablecomingsoonupsell,enableconsolepcsearch,enableconsoles,enablecontextualstorebrowse,enablecontrollerstatusv2,enablecontrollervibration,enabledefaultultimateupsell,enabledisconnectwarning,enableenhancedreportareview,enablefeedbacksdk,enablefriendlinksharing,enablefriendsandfollowers,enablegameinvites,enablegamingconsentservicesettings,enablegarrisoninlineredeem,enablegcs,enablegen8deprecationwave1,enablegen8deprecationwave2,enablegtaplus,enableguidechattab,enableguidehometab,enableguidenotifications,enableguideprofiletab,enablehhverified,enableiapbrowseexperience,enableinternalcookielist,enablejanus,enablejanusxboxcom,enablelaunchpad,enablelaunchpadupdates,enableleavingdate,enableloginsagafix,enablemaunaloa,enablemecontrolgamerscore,enablemecontrolpresence,enablemediaplayonweb,enablemessagesafetysettings,enablemiconmacsafari,enableminipdprefreshexp,enablemouseandkeyboard,enablemulticloudplaybutton,enablemultiupsellbutton,enablemutualfriendsprivacysettings,enablenakatomi,enablenakatomiu,enablenetqualityindicator,enablenewsearchexperience,enablenewsearchgeneraltab,enableoffersandcredits,enableopenendedgameinvites,enableoverridedevsettings,enableparties,enablepcgp,enablepdpgallery,enablepidlstandarizedforms,enableplaypathnavigation,enableplaywithfriendsrow,enablepresenceheartbeat,enableprivacycontrols,enableprovisioningupsell,enablereactcheckout,enablereactgiftflow,enablereactredeem,enablerealnamesharing,enableredeemcodemodal,enableremoteplay,enablesearchpagev2,enablesearchpromo,enablesenerchia,enablesessiontime,enablesiglv3,enablestorebyog,enablestreamstatistics,enablesubscriptionpromotionaltag,enabletakcontrolresizing,enabletakhighcontrastmode,enabletitanautorenewtoggle,enabletitanredeemsubs,enabletitleactivation,enabletulipedgewater,enabletvautosignout,enabletvgamepassupsellv2,enabletvlayerhint,enableubisoftpcversionlegaltext,enableubisoftplusdata,enableusbguidance,enableuseretryafterheader,enableuserprofilepage,enableuserrequestedres,enableuserstoragemenu,enablewishlistgifting,enablexboxapponmobilegooglepay,enablexboxcomnewui,enablexboxcomredeemhostnor,enablexboxgamepadlite,enablexboxonerfaccountsettings,enablexboxonerfsetupredirectpage,enablexboxsmallpurchasedialog,enablexesurveys,enablexgpp,enablexsearch,enablextracetelemetry,flight_6_1_446,hidebetareferences,purchasesdkcartcheckout,randomizeentitlementquery,routev2,showmousekeyboardsetting,skipredirectcounter,testautomaticxboxwebexpscorecard,test_flight_7_11_752,usegearsinsiderapi,uselocalorigininvitelinks,usepostmessagehelper,usetizenh264mainsdphack,usev2msaxblauth,xwsrmdevaa50,xwsrmdevaa90',
        }

        params = {
            'locale': 'en-IN',
        }

        json_data = {
            'Filters': 'eyJHZW5yZSI6eyJpZCI6IkdlbnJlIiwiY2hvaWNlcyI6W3siaWQiOiJTdHJhdGVneSJ9XX0sIlBsYXlXaXRoIjp7ImlkIjoiUGxheVdpdGgiLCJjaG9pY2VzIjpbeyJpZCI6Ilhib3hTZXJpZXNYfFMifSx7ImlkIjoiWGJveE9uZSJ9LHsiaWQiOiJDbG91ZEdhbWluZyJ9LHsiaWQiOiJYYm94UGxheUFueXdoZXJlIn1dfX0=',
            'ReturnFilters': False,
            'ChannelKeyToBeUsedInResponse': 'BROWSE_CHANNELID=_FILTERS=GENRE=STRATEGY&PLAYWITH=CLOUDGAMING,XBOXONE,XBOXPLAYANYWHERE,XBOXSERIESX|S',
            'EncodedCT': encodeCT,
            'ChannelId': '',
        }

        response = requests.post('https://emerald.xboxservices.com/xboxcomfd/browse', params=params, headers=headers, json=json_data)

        if response.status_code ==200:
            json_data = response.json()
            broswer_channel_data = list(json_data.get("channels").values())[0]
            if broswer_channel_data.get('encodedCT'):
               new_encodeCT = broswer_channel_data.get('encodedCT')
            else:
               new_encodeCT = None

            if json_data.get("skuSummaries"):
                for item in json_data.get("skuSummaries"):
                    titlename = item.get("skuTitle") or ""
                    slugname = slugify(titlename)

                    if not slugname:
                        slugname = "product"

                    url = f"{base_url.rstrip('/')}/{slugname}/{product_id}/{sku_id}"
                    titles.append({
                        "product_id": item.get("productId"),
                        "title": item.get("skuTitle"),
                        "sku_id": item.get("skuId"),
                        "url" : url
                    })
            return new_encodeCT
        else:
            print("Error", response.status_code)
            return None


response = requests.get(
    'https://www.xbox.com/en-IN/games/all-games/console?PlayWith=XboxSeriesX%7CS,XboxOne,CloudGaming,XboxPlayAnywhere&Genre=Strategy', 
    params=params,
    headers=headers,
    impersonate="chrome120"
)

if response.status_code == 200:
    html_data = Selector(response.text)

    # Find the script containing PRELOADED_STATE
    script_text = html_data.xpath(
        "//script[contains(text(),'__PRELOADED_STATE__')]/text()"
    ).get()

    if script_text:
        match = re.search(
            r'window\.__PRELOADED_STATE__\s*=\s*(\{.*?\})\s*;',
            script_text,
            re.DOTALL
        )

        if match:
            data = json.loads(match.group(1))

            products = data["core2"]["products"]["productSummaries"]
            availability = data["core2"]["products"]["availabilitySummaries"]
            channelData = jmespath.search("core2.channels.channelData",data)
            channelDataValues = list(channelData.values())
            encodeCT = jmespath.search('data.encodedCT',channelDataValues[0])


            for product_id, product_data in products.items():

                sku_id = None

                if product_id in availability:
                    for market_data in availability[product_id].values():
                        for availability_info in market_data.values():
                            sku_id = availability_info.get("price", {}).get("skuId")
                            break
                        if sku_id:
                            break
                titlename = product_data.get("title") or ""

                slugname = slugify(titlename)

                if not slugname:
                    slugname = "product"

                url = f"{base_url.rstrip('/')}/{slugname}/{product_id}/{sku_id}"
                print(url)
                titles.append({
                    "product_id": product_id,
                    "title": product_data.get("title"),
                    "sku_id": sku_id,
                    "url": url
                })

            while encodeCT:
                print("Fetching next page...")
                encodeCT = getdataFromApi(encodeCT)

            print("Total titles:", len(titles))

            with open("titles.json", "w", encoding="utf-8") as f:
                json.dump(titles, f, ensure_ascii=False, indent=4)

            with open("scripts.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print(f"Saved {len(titles)} titles")
            print("JSON saved successfully")