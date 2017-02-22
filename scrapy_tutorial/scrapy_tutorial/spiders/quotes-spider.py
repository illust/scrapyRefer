"""
reated on Tue Feb 21 09:32:10 2017

@author: thor
"""

import scrapy

#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#            
#          
#    start_urls = [
#        'http://quotes.toscrape.com/page/1',
#        ]
#                                        
#    def parse(self,response):
#        for quote in response.css('div.quote'):
#        yield{
#                'text':quote.css('span.text::text').extract_first(),
#                'author':quote.css('small.author::text').extract_first(),
#                'tags':quote.css('div.tags a.tag::text').extract(),
#            }
#                  

class Myspider(scrapy.Spider):
    name = 'mySpider'
    
    def start_requests(self):
        return [scrapy.FormRequest("http://www.example.com/login",
                                   formdata={'user':'john','pass':'secret'},
                                            callback=self.logged_in)]
    
    def logged_in(self,response):
        pass
                                                                                                                                      
                                                                                                                                                                next_page = response.css('li.next a::attr(href)').extract_first()
                                                                                                                                                                        if next_page is not None:
                                                                                                                                                                                    next_page = response.urljoin(next_page)
                                                                                                                                                                                                yield scrapy.Request(next_page,callback=self.parse)
