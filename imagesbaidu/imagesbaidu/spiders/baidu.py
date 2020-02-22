# -*- coding: utf-8 -*-
import scrapy
import re
import json
from imagesbaidu.items import ImagesbaiduItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.image.baidu.com']

    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%8B%E8%97%A4%E9%A3%9E%E9%B8%9F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E6%96%8B%E8%97%A4%E9%A3%9E%E9%B8%9F&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1556288487507="

    start_urls = [url]



    def parse(self, response):
        # print(response.text)

        pattern = re.compile(r'"middleURL":"(.*?)"', re.S)

        datas = re.findall(pattern, response.text)



        for data in datas:
            item = ImagesbaiduItem()
            item['image_urls'] = data
            yield item



