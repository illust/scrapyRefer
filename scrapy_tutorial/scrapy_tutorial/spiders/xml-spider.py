#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:16:43 2017

@author: thor
"""

from scrapy import log
from scrapy.spiders import XMLFeedSpider
from scrapy_tutoria.items import TestItem

class MySpider(XMLFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iternodes' #This is actually unnecessary,since it's the default value
    itertag = 'item'
    
    def parse_node(self,response,node):
        log.msg('Hi,this is a <%s> node!: %s' % (self.itertag,''.join(node.extract())))

        item = TestItem()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item
    
    
    
    











