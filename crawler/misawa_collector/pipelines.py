# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import os
from PIL import Image
from io import StringIO
import requests

class MisawaCollectorPipeline(object):
    def process_item(self, item, spider):
        """ item: {'name':str, 'url'}
        """

        # create name directory
        img_dir = os.path.join('images', item['name'])
        os.makedirs(img_dir, exist_ok=True)

        # download image
        #res = requests.get(item['url'])
        #img_cnt = StringIO(res.text)
        #img = Image.open(img_cnt)
        res = requests.get(item['url'], stream=True)
        img = Image.open(res.raw)

        # create image name
        img_name = item['url'].split('/')[-1]
        img_path = os.path.join(img_dir, img_name)
        img.save(img_path)
        return item
