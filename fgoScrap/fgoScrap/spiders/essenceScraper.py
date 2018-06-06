import scrapy

from fgoScrap.items import EssenceItem

#scrapy crawl essencelist -o [nom-de-loutput].json
class EssenceScraper(scrapy.Spider):
    name = "essencelist"

    custom_settings = {
        'ITEM_PIPELINES': {
            'fgoScrap.pipelines.EssencePipeline': 400
        }
    }

    def start_requests(self):
        urls = [
            'https://fate-go.cirnopedia.org/craft_essence.php?JP=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for row in response.xpath('//table[@id="rounded-corner"]/tbody/tr[@class="reg US"]'):
            item = EssenceItem()
            item['name'] = row.xpath('td[4]/@sorttable_customkey').extract()
            item['stars'] = row.xpath('td[2]/text()').extract()
            item['image_url'] = row.xpath('td[3]/a/img/@style').extract()
            yield item

