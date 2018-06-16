# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FgoscrapPipeline(object):
    def process_item(self, item, spider):
        return item


class ServantPipeline(object):
    def process_item(self, item, spider):
        item['name'] = item['name'][0]

        item['stars'] = item['stars'][0][:1]

        item['sclass'] = item['sclass'][0][:-1]

        full_url = item['image_url'][0]
        servant_url = full_url.split(",")[2]
        item['image_url'] = "https://fate-go.cirnopedia.org/"+servant_url[7:-2]

        return item

class EssencePipeline(object):
    def process_item(self, item, spider):
        item['name'] = item['name'][0]

        item['stars'] = item['stars'][0][:1]

        full_url = item['image_url'][0]
        servant_url = full_url.split(",")[2]
        item['image_url'] = "https://fate-go.cirnopedia.org/"+servant_url[6:-3]

        return item