# -*- coding: utf-8 -*-
import scrapy

with open('websites.txt','r') as reader:
    x = reader.read()
    print(x)

class CollectemailSpider(scrapy.Spider):
    name = 'collectemail'
    start_urls = ['http://www.rougecalgary.com/']

    def parse(self, response):
        pass
