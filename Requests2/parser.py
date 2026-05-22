# Parses page response into a structured format
from parsel import Selector
from xpaths import CATEGORY_LINK_BOX_XPATH

def main_page_parse(content):
    try:
        selector = Selector(body=content)
        all_links = list()
        for category_elm in selector.xpath(CATEGORY_LINK_BOX_XPATH):
            link = category_elm.xpath('.//a/@href').getall()
            all_links.append(link)
        
        return {
            "data": all_links,
            "error": None
        }
    except Exception as e:
        return {
            "data": [],
            "error": str(e)
        }

def listing_page_parse(content):
    try:
        selector = Selector(body=content)
       
        
        return {
            "data": "",
            "error": None
        }
    except Exception as e:
        return {
            "data": [],
            "error": str(e)
        }
    

def product_page_parse(content):
    try:
        selector = Selector(body=content)
       
        
        return {
            "data": "",
            "error": None
        }
    except Exception as e:
        return {
            "data": [],
            "error": str(e)
        }