# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from splash_gcs.items import SplashGcsItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['www.uniqlo.com']
    start_urls = [('https://www.uniqlo.com/jp/store/search?'
                   'groupby=item_id&text-index=%E3%83%8B%E3%83%83%E3%83%88&'
                   'type_cd_search-index=men&cat1_cd_search-index=&'
                   'cat2_cd_search-index=&badges_id_inf_search-index=&'
                   'size_cd-in=&color_cd-in=&sale_price-numberrange=&'
                   'sortcolumn=&offset=&qbrand=20')]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        item = SplashGcsItem()
        item['file_urls'] = [response.urljoin(img) for img in
                             response.xpath('//dd[@class="thumb"]//img/@src').extract()]
        yield item
