"""
reated on Tue Feb 21 09:32:10 2017

@author: thor
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
            
          
    start_urls = [
        'http://quotes.toscrape.com/page/1',
        ]
                                        
    def parse(self,response):
        for quote in response.css('div.quote'):
        yield{
                'text':quote.css('span.text::text').extract_first(),
                'author':quote.css('small.author::text').extract_first(),
                'tags':quote.css('div.tags a.tag::text').extract(),
            }
                  

class Myspider(scrapy.Spider):
    name = 'mySpider'
    
    def start_requests(self):
        return [scrapy.FormRequest("http://www.example.com/login",
                                   formdata={'user':'john','pass':'secret'},
                                            callback=self.logged_in)]
    
    def logged_in(self,response):
        pass
    

class MySpider(scrapy.Spider):
    name = 'myspider'
    
    def __init__(self,category=None,*args,**kwargs):
        super(MySpider,self).__init__(*args,**kwargs)
        self.start_urls = ['http://www.example.com/categories/%s' % category]
#super() use to avoid the parent class name
        
     
#For the examples used in the following spiders, we’ll assume you have a project with a TestItem declared in a
#myproject.items module
import scrapy

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    
    
#Let’s now take a look at an example CrawlSpider with rules
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']
    
    rules = (
        # Extract links matching 'category.php'(but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow('category\.php',),deny=('subsection\.php',))),
            
        #Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow('item\.php',)),callback='parse_item'),
            )
    
    def parse_item(self,response):
        self.logger.info('Hi,this is an item page! %s',response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
















                                                                                                                                      
                                                                                                                                                                next_page = response.css('li.next a::attr(href)').extract_first()
                                                                                                                                                                        if next_page is not None:
                                                                                                                                                                                    next_page = response.urljoin(next_page)
                                                                                                                                                                                                yield scrapy.Request(next_page,callback=self.parse)
