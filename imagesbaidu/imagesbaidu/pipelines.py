# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline


class ImagesbaiduPipeline(object):
    def process_item(self, item, spider):
        return item


class BaiduPipeline(ImagesPipeline):
    default_headers = {
        "Accept": "text/plain, */*; q=0.01",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,ja;q=0.7",
        "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%96%8B%E8%97%A4%E9%A3%9E%E9%B8%9F&oq=%E6%96%8B%E8%97%A4%E9%A3%9E%E9%B8%9F&rsp=-1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    }

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    # 第一个item对象是爬取生成的Item对象，可以将他的url字段取出来，直接生成scrapy.Request对象,此Request加入到调度队列，等待被调度，然后执行下载
    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            if item.__class__.__name__ != "ImagesbaiduItem":
                return
            for image_url in item["image_urls"]:
                yield scrapy.Request(url=image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):

        if item.__class__.__name__ != "ImagesbaiduItem":
            return item

        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("没有下载到图 Image Dowload Failed")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
