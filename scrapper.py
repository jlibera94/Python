from bs4 import BeautifulSoup 
from csv import writer
import requests

page_link = 'https://montreal.craigslist.ca/d/apts-housing-for-rent/search/apa?lang=en&cc=us'

#get the content from url
page_response = requests.get(page_link, timeout=5)

#parse html
page_content = BeautifulSoup(page_response.content,"html.parser")

#extraction of all html elements where price is stored
prices = page_content.find_all(class_='result-price')


prices = page_content.find_all('div', attrs={'class':'result-price'})






