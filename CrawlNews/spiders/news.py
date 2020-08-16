# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from newsplease import NewPlease
from CrawlNews.items import CrawlnewsItem

class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['vnexpress.net']
    start_urls = ['http://vnexpress.net/']

    rules = (
        Rule(LinkExtractor(allow_domains=['vnexpress.net']), callback='parse_item', follow=True),
    )

    def __init__(self, crawlMode='', **kwargs):
        super().__init__(**kwargs)
        self.crawlMode = crawlMode

    def start_request(self):
        yield scrapy.Request(url=self.crawlMode, callback=self.parse_item)


    def parse_item(self, response):
        article = NewPlease.from_url(response.url)
        item = CrawlnewsItem()
        item['title'] = article.title
        item['url'] = response.url
        yield item
