# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DiariosSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    files_urls = scrapy.Field()
    files = scrapy.Field()

import scrapy


class Gazette(scrapy.Item):
    source_text = scrapy.Field()
    date = scrapy.Field()
    edition_number = scrapy.Field()
    file_checksum = scrapy.Field()
    file_path = scrapy.Field()
    file_url = scrapy.Field()
    file_requests = scrapy.Field()
    is_extra_edition = scrapy.Field()
    territory_id = scrapy.Field()
    power = scrapy.Field()
    scraped_at = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()