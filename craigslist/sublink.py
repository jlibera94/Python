# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:21:05 2019

@author: jlibe

"""
# =============================================================================
# 
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#  
#  
# def get_website_info(response):
#     bs_obj = BeautifulSoup(response, "html.parser")
#     if bs_obj:
#         # Buyer info for current_page        
#         get_buyer_info(bs_obj)
#         all_pages = bs_obj.find_all("a")
#         links = set()
#         for page in all_pages:
#             links.add(page["href"])
#         if links:
#                 # Buyer info for remaining pages            
#               for next_page in links:
#                  page_response = urlopen(url=next_page)
#                  bs_obj = BeautifulSoup(page_response,	"html.parser")
#                  get_buyer_info(bs_obj)
#  
#  
# def get_buyer_info(bs_obj):
#     buyer_info = bs_obj.find_all("div", {"title": "buyer-info"})
#     if buyer_info:
#         for tag in buyer_info:
#             buyer_name = tag.find("div", {"title": "buyer-name"}).text
#             item_price = tag.find("span", {"class": "item-price"}).text
#             print(buyer_name, item_price)
#             
# if __name__ == "__main__":
#     res = urlopen("http://econpy.pythonanywhere.com/ex/001.html")
#     get_website_info(res)
# =============================================================================

from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_website_info(response):
    bs_obj = BeautifulSoup(response, "html.parser")
    if bs_obj:
        #info on current page
        get_post_info(bs_obj)
        all_pages = bs_obj.find_all("link", {"rel":"canonical"})
        #links = set()
        links = []
        for page in all_pages:
            links.append(page["href"])
            
        if links:
            #info for remaining pages
              for next_page in links:
                  page_response = urlopen(url = next_page)
                  bs_obj = BeautifulSoup(page_response, "html.parser")
                  get_post_info(bs_obj)
                
def get_post_info(bs_obj):
    post_info = bs_obj.find_all("h2", {"class":"postingtitle"})

    if post_info:
        for tag in post_info:
            title_post = tag.find("span", {"id": "titletextonly"}).text
            print(title_post)
    
if __name__ == "__main__":
      res = urlopen("https://montreal.craigslist.org/apa/d/montreal-magnigique-condo-neuf/6790797630.html?lang=en&cc=us")
      get_website_info(res)