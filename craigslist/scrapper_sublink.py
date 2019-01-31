# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:19:02 2019

@author: John
"""

import bs4
import requests
import os, os.path, csv
from csv import writer
import re

def title_formatter(format_input):
    return format_input

def price_formatter(price):
    price = price.replace("$","")
    return '$' + price.strip()

def address_formatter(address):
    return address

def request_bs(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return soup

url = 'https://montreal.craigslist.org/search/apa?lang=en&cc=us'

#opening csv file
file_name = 'craigslist_info.csv'
with open(file_name, 'w+') as output_file:
    csv_writer = writer(output_file, delimiter=',')
    csv_writer.writerow(["Title", "Price", "Address"])
    
soup = request_bs(url)

informationDIV = soup.select('li result-row')
length = len(informationDIV)


MAXIMUM = 100
start = 0
while start < 100:
    number_of_articles = len(soup.select('li result row'))
    for i in range(len(informationDIV)):
        try:
            start = start + 1
            titles = soup.select('li result-row > .result-title > a')
            
           #get titles
            title = title_formatter(titles[i].getText())
            
            #checking each element's detail
            sublink = 'https://montreal.craigslist.org/' + titles[i].get('href')
            subsoup = request_bs(sublink)
            #please refer to price_formatter function
            price = price_formatter(subsoup.select_one('span[class*="result-price"]').text)
            
            address = address_formatter(subsoup.select_one('span[class*="result-hood"]').text)
            
        except:
            pass
        
        with open(file_name, "a", encoding='UTF-8') as output_file:
            csv_writer = writer(output_file, delimeter=',')
            csv_writer.writerow([title, price, address])
      
    try:    
        nextpageLink = soup.select('a[title="next page"]')[0]
    except:
        pass
    
    url = 'https://montreal.craigslist.org/' + nextpageLink.get('href')
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

output_file.close()         