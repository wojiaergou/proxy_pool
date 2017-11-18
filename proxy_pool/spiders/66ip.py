# -*- coding: utf-8 -*-
# __author__: vincentlc

import scrapy
from proxy_pool.items import ProxyPoolItem


class SixSixIpSpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['66ip.cn']
    start_urls = ["http://www.66ip.cn/areaindex_1/1.html"]

    def start_requests(self):
        for i in range(1, 35):
            for j in range(1, 4):
                yield scrapy.Request("http://www.66ip.cn/areaindex_{0}/{1}.html".format(i, j),
                                     callback=self.parse)

    def parse(self, response):

        iplist = response.xpath('//*[@id="footer"]/div/table//tr')

        for x in iplist[1:-1]:
            ips = x.xpath('td[1]/text()').extract()[0]
            ports = x.xpath('td[2]/text()').extract()[0]
            protocols = 'HTTP'
            address = x.xpath('td[3]/text()').extract()[0]
            types = x.xpath('td[4]/text()').extract()[0]

            yield ProxyPoolItem({
                'ip': ips,
                'protocol': protocols,
                'port': ports,
                'types': types,
                'address': address,
                'website': 'www.66ip.cn'
            })
