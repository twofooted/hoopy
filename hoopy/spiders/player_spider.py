import time
import scrapy


class PlayerSpider(scrapy.Spider):
    name = "player"

    start_urls = [
        'https://www.basketball-reference.com/players/j/jamesle01.html',
    ]

    def parse(self, response):
        gamelog_urls = response.xpath('//tbody/tr/th/a/@href').extract()

        for url in gamelog_urls:
            time.sleep(1)
            yield response.follow(url, callback=self.parse_stats)
    
    def parse_stats(self, response):
        rows = response.xpath('//table[@id="pgl_basic"]/tbody/tr')

        for row in rows:
            yield {
                'minutes': row.xpath('td[@data-stat="mp"]/text()').extract_first(),
                'date': row.xpath('td[@data-stat="date_game"]/a/text()').extract_first(),
                'fta': row.xpath('td[@data-stat="fta"]/text()').extract_first()
            }
