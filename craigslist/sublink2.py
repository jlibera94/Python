# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:08:49 2019

@author: John
"""
import scrapy
from scrapy.http import Response, Request


class MultipleQuotesPaginationSpider(scrapy.Spider):
    name = "multiple-craigslist-pagination"
    allowed_domains = ["craigslist.org"]
    start_urls = ['https://montreal.craigslist.org/apa/d/montreal-juillet-rosemont-luxueux-3-cac/6803815041.html?lang=en&cc=us']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for post in response.css('span.postingtitletext'):
            item = {
                'price': post.css('span.price::text').extract_first(),
          #      'text': data.css('span.text::text').extract_first(),
          #      'tags': data.css('a.tag::text').extract(),
            }
            yield item
        # follow pagination link
        next_page_url = response.css('div.prevnext js-only show-prevnext > a.next::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)