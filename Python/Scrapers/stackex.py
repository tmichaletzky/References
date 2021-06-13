import scrapy
import time
import sys, json
import socket
import requests


class MathstackSpider(scrapy.Spider):
    name = 'mathstack'
    allowed_domains = ['math.stackexchange.com']
    start_urls = ['https://math.stackexchange.com/questions?tab=votes']
     
    def parse(self, response):
        for entry in response.css('div.question-summary'):
            #url = entry.css('a.question-hyperlink::attr(href)').get()
            title = entry.css('a.question-hyperlink::text').get()
            user = entry.css('div.user-details a::text').get()
            tags = entry.css('a.post-tag::text').getall()
            time = entry.css('span.relativetime::attr(title)').get()
            
        for stat in response.css('div.statscontainer'):
            votes = stat.css('span.vote-count-post ::text').get()
            answers = stat.css('div.status.answered::text').get()
            views = stat.css('div.views ::text').get()
        
        try:
            answers = answers.strip('\r\n').strip(' ')
        except AttributeError:
            pass
        
        try:
            views = views.strip('\r\n').rstrip('views').strip(' ')
        except AttributeError:
            pass        
        
            
        yield{
                #'url': response.urljoin(url),
                'title': title,
                'user': user,
                'tags': tags,
                'time': time,
                'votes': votes,
                'answers': answers,
                'views': views
            }        

        next_page = response.css('div.s-pagination.pager.fl a.s-pagination--item.js-pagination-item::attr(href)').getall()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)