# -*- coding: utf-8 -*-
import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    start_urls = ['https://www.diariomunicipal.com.br/amm-mg/']

    def parse(self, response):
        link = response.css('#downloadPdf ::attr(href)').get()
        yield{
            'Title':'Diario',
            'file_urls':[link]
        }
