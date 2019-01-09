# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:21:05 2019

@author: jlibe

"""

from bs4 import BeautifulSoup
import urllib.request

for numb in ('1', '10'):
    resp = urllib.request.urlopen("https://montreal.craigslist.org/search/apa?lang=en&cc=us")
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

    for link in soup.find_all('a', href=True):
        print(link['href'])
# =============================================================================
# import requests
# import csv
# import time
# from bs4 import BeautifulSoup
# 
# res = requests.get('https://montreal.craigslist.org/search/apa?lang=en&cc=us')
# 
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# 
# all_links = soup.find_all('a')
# 
# for link in all_links:
#     print(link.get("href"))
# =============================================================================

# =============================================================================
# result = soup.find('p', class_='result-info')
# title_post = result.a.text
# print(title_post)
# =============================================================================



# =============================================================================
# csv_file = open('sublink_apt.csv','w')
# 
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow
# 
# domains = soup.find_all("span", class_="result-title hdrlnk")
# 
# =============================================================================
#We need Price, address, postal code