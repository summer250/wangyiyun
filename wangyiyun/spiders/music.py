# -*- coding: utf-8 -*-
import re
import json
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wangyiyun.items import WangyiyunItem


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    # start_urls = ['http://music.163.com/']

    def start_requests(self):
        item = WangyiyunItem()

        options = Options()
        options.add_argument('-headless')
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('https://music.163.com/#/discover/toplist?id=3778678')
        browser.switch_to.frame("contentFrame")
        html_source = browser.page_source
        id_list = re.findall('<div class="opt hshow">(.*?)</div>', html_source, re.S)
        browser.quit()
        for id in id_list:
            number = re.findall('''<span data-res-id="(.*?)" data-res-type="18" data-res-action="fav"''', id)
            number = "".join(number)
            item["id"] = number
            start_urls = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(number)
            yield scrapy.Request(url=start_urls,callback=self.parse_data,meta={"item":item})

    def parse_data(self, response):
        item = response.meta["item"]

        html = response.text
        json_data = json.loads(html)
        results = json_data["hotComments"]
        for result in results:
            content = result['content']
            item["content"] = content
            print(item)
        yield item




