from parsel import Selector
from xpaths import BROWSE_ALL_APPLE_SCRIPT_PATH, BROWSE_SUB_CAT_SCRIPT_PATH, ITEM_PATH
from rich import print
import json
import jmespath

def get_home_page_cat_link(is_success, content):
  category_links = []
  if is_success:
    html_content = Selector(text=content)
    script_data = json.loads(html_content.xpath(BROWSE_ALL_APPLE_SCRIPT_PATH).get())
    category_data = jmespath.search('data[1].data.shelves[7].items[*]', script_data)
    for category in category_data:
      category_links.append({
        "category_name": jmespath.search('title',category).replace('\ufeff', '').replace('\xa0', ' '),
        "category_url": jmespath.search('contextAction.url', category),
      })
    return category_links
  else:
    return (f"something wrong with response : {is_success} : function(get_home_page_cat_link)")

def get_sub_cat_links(is_success, content):
  all_sub_cat_links = []
  if is_success:
    html_content = Selector(text=content)
    script_data = json.loads(html_content.xpath(BROWSE_SUB_CAT_SCRIPT_PATH).get())
    # with open("./scraped_data/sub_cat_data.json", 'w', encoding='utf-8') as f:
    #   json.dump(script_data, f, indent=2)
    sub_cat_data = jmespath.search('data[1].data.shelves[*]', script_data)
    for data in sub_cat_data[2:]:
      if jmespath.search('items', data):
        all_sub_cat_links.append({
          "sub_category_name": "Recent" if not jmespath.search('impressionMetrics.fields.name', data) else jmespath.search('impressionMetrics.fields.name', data),
          "items": [
            {
              "title": jmespath.search('title', item) if not jmespath.search('title', item) is None else jmespath.search('contextAction.title', item),
              "url": jmespath.search('segue.url', item) if not jmespath.search('segue.url', item) is None else jmespath.search('contextAction.url', item),
            } for item in jmespath.search('items[*]', data) if jmespath.search('title',item)
          ]
        })
    return all_sub_cat_links
  else:
    return (f"something wrong with response : {is_success} : function(get_sub_cat_data)")

def get_item_data(is_success, content):
  items_data = {}
  if is_success:
    html_content = Selector(text=content)
    script_data = json.loads(html_content.xpath(ITEM_PATH).get())
    with open("./scraped_data/get_item.json", 'w', encoding='utf-8') as f:
      json.dump(script_data, f, indent=2)
    shelves = jmespath.search('data[1].data.shelves[*]',script_data)
    # # get main page of item
    for shelve in shelves:
      if 'canonical-header' in jmespath.search('id', shelve):
        items_data['BannerData'] = {
          "item_title": jmespath.search('items[0].title', shelve),
          "item_description": jmespath.search('items[0].description', shelve),
          "tags": jmespath.search('items[0].primaryMetadata', shelve),
          "year": jmespath.search('items[0].badgeRowMetadata[0]', shelve),
          "duration": jmespath.search('items[0].badgeRowMetadata[1]', shelve),
          "thumb_image" : jmespath.search('items[0].contentLogo.template', shelve).replace(r"{w}", str(jmespath.search('items[0].contentLogo.width', shelve))).replace(r"{h}", str(jmespath.search('items[0].contentLogo.height', shelve))).replace(r"{f}", 'webp')
        } 
      
    #   # get episodes
      elif 'EpisodeList' in jmespath.search('id', shelve):
        items_data['Episodes'] = [
          {
            "item_tag": jmespath.search('tag',item),
            "item_title": jmespath.search('title', item),
            "description": jmespath.search('description', item),
            "episode_url": jmespath.search('segue.url', item),
          }
            for item in jmespath.search('items[*]', shelve)
        ]

      
    #   # get trailers
      elif 'Trailers' in jmespath.search('id', shelve):
        items_data['Trailers'] = [
          {
            "item_title": jmespath.search('title',item),
            "url": jmespath.search('segue.url',item),
            "duration": jmespath.search('metadata', item)
          }
            for item in jmespath.search('items[*]', shelve)
        ]

    return items_data
      
def get_upcomming_show_data(is_success, content):
  if is_success:
    html_content = Selector(text=content)
    script_data = json.loads(html_content.xpath(BROWSE_ALL_APPLE_SCRIPT_PATH).get())
    upcoming_data = {}
    for shelve in jmespath.search('data[1].data.shelves[*]', script_data):
      if 'epicStageWithUpsell' in jmespath.search('"$type"', shelve):
        upcoming_data['BannerData'] = [
          {
            "item_title": jmespath.search('title', item),
            "item_description": jmespath.search('description', item),
            "tags": jmespath.search('primaryMetadata', item),
            "year": jmespath.search('badge', item),
            "thumb_image" : jmespath.search('artwork.wide.template', item).replace(r'{w}', '2400').replace(r'{h}', '1350').replace(r'{f}', 'webp')
          }
          for item in jmespath.search("items", shelve)
        ]
      elif 'trailerLockup' in jmespath.search('"$type"', shelve):
        upcoming_data['Trailers'] = [
          {
            "item_title": jmespath.search('contextAction.title',item),
            "url": jmespath.search('contextAction.url',item),
            "tags": jmespath.search('metadata', item)
          }
            for item in jmespath.search('items[*]', shelve)
        ]
      elif 'lockup' in jmespath.search('"$type"', shelve):
        upcoming_data['Upcomming_origins'] = [
          {
            "item_title": jmespath.search('contextAction.title', item),
            "url": jmespath.search("contextAction.url", item),
            "tags": jmespath.search("type", item)
          } for item in jmespath.search('items[*]', shelve)
        ]
    return upcoming_data
