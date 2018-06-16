import scrapy

from fgo.fgoScrap import ServantItem


#scrapy crawl servantlist -o [nom-de-loutput].json
class ServantScraper(scrapy.Spider):
    name = "servantlist"

    custom_settings = {
        'ITEM_PIPELINES': {
            'fgoScrap.pipelines.ServantPipeline': 400
        }
    }

    def start_requests(self):
        urls = [
            'https://fate-go.cirnopedia.org/servant_all.php?JP=0#nav'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for row in response.xpath('//table[@id="rounded-corner"]/tbody/tr[@class="US"]'):
            item = ServantItem()
            item['name'] = row.xpath('td[4]/@sorttable_customkey').extract()
            item['stars'] = row.xpath('td[2]/text()').extract()
            item['sclass'] = row.xpath('td[5]/text()').extract()
            item['image_url'] = row.xpath('td[3]/a/div/@style').extract()
            yield item