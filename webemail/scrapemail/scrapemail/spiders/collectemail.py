# -*- coding: utf-8 -*-
import scrapy
import re


class CollectemailSpider(scrapy.Spider):
    name = 'collectemail'

    web = open('websites.txt')
    lis = list(web)
    start_urls = [i for i in lis]

    def parse(self, response):
        Url = response.request.url
        try:
            emails = re.findall("[A-Za-z0-9._-]+@[a-z0-9_-]+[.]+[a-z]+", str(response.body))
            if emails != []:
                uniquemail = set(emails)
                mail = set()
                for i in uniquemail:
                    if i.endswith('png') or i.endswith('jpg') or i.endswith('gif') or i.endswith('press') or i.endswith('food') or i.endswith('time') or i.endswith('test.com') or i.endswith('mail.com') or i.endswith('example.com') or i.endswith('press.io'):
                        continue
                    else:
                        mail.add(i)
                emailid = " | ".join(mail)
            else:
                contact = response.xpath('//a[contains(@href,"contact")]/@href').get()
                contactlink = response.urljoin(contact)
                yield scrapy.Request(contactlink, callback=self.parse)
                # emailid = 'N/A'
        except:
            pass
        if emailid != '':
            yield {'Email':emailid, "Url":Url}
