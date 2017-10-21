# -*- coding=utf-8 -*-
"""
"""

import scrapy

class CharaSpider(scrapy.Spider):
    name='chara'
    start_urls = ['http://jigokuno.com']

    def parse(self, response):
        for article in response.css("article"):
            name = article.css("div.article-category a::text").extract_first() 
            url = article.css("div.article-body-inner a::attr(href)").extract_first()
            
            if url is None:
                url = article.css("div.article-body-inner img::attr(src)").extract_first()
            
            yield {
                'name' : name,
                'url' : url,
            }
            
        next_page = response.xpath("//a[@rel='next']/@href").extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
