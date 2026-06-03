from scripts.fetch import CallRequests
from config import APPLE_TV_HEADERS, APPLE_TV_URL,FILE_PATH, APPLE_TV_PARAMS
from rich import print
from parser import get_home_page_cat_link, get_sub_cat_links, get_item_data, get_upcomming_show_data
total_movie_links = 0

apple_tv_data = []

apple_tv = CallRequests(headers=APPLE_TV_HEADERS, path=FILE_PATH)
res = apple_tv.fetch_requests(url=APPLE_TV_URL, method='GET')
if['is_success']:
  home_category_data = get_home_page_cat_link(is_success=res['is_success'], content=res['body'])


for category_data in home_category_data:
  print("category name :", category_data.get('category_name'), "||", "category url :", category_data.get('category_url'))
  sub_cat_data = []
  if '/room/coming-to-appletv/' in category_data.get('category_url'):
    res = apple_tv.fetch_requests(url=category_data.get('category_url'), method="GET")
    sub_cat_data.append(
      {
          "data": get_upcomming_show_data(is_success=res['is_success'], content=res['body'])
      })
    total_movie_links += len(sub_cat_data[-1].get('data').get('Upcomming_origins'))
    print(sub_cat_data)
  else:
    res = apple_tv.fetch_requests(url=category_data.get('category_url'), method="GET")
    all_sub_cat_links = get_sub_cat_links(is_success=res['is_success'], content=res['body'])
    for sub_cat_link in all_sub_cat_links:
      total_movie_links += len(sub_cat_link.get('items'))
      print("--> sub cat title : ", sub_cat_link.get('sub_category_name'), ":", sub_cat_link.get('items'))
      sub_cat_data.append(
        {
          "sub_category_header": sub_cat_link.get('sub_category_name'),
          "sub_category_data": [
            {
              "sub_title": sub_links.get('title'),
              "sub_url": sub_links.get('url'),
              "sub_data": get_item_data(
                is_success=apple_tv.fetch_requests(url=sub_links.get('url'), method="GET")['is_success'],
                content=apple_tv.fetch_requests(url=sub_links.get('url'), method="GET")['body'],
                ) if sub_links.get('url') else {}
            }
            for sub_links in sub_cat_link.get('items')
          ]
        })
  apple_tv_data.append(
    {
      "category_name": category_data.get('category_name'),
      "category_url": category_data.get('category_url'),
      "category_data": sub_cat_data
    }
  )

apple_tv.save_data_into_file(content=apple_tv_data, file_name='apple_tv_data.json')
print("Total movies links : ",total_movie_links)