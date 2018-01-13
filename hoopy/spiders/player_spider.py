import scrapy
import time

class PlayerSpider(scrapy.Spider):
    name = "player"

    start_urls = [
        'https://www.basketball-reference.com/players/j/jamesle01.html',
    ]

    def parse(self, response):
        gamelog_urls = response.xpath('//tbody/tr/th/a/@href').extract()

        for url in gamelog_urls:
            time.sleep(2)
            yield response.follow(url, callback=self.parse_stats)
    
    def parse_stats(self, response):
        rows = response.xpath('//table[@id="pgl_basic"]/tbody/tr')
        title = response.xpath('//h1[@itemprop="name"]/text()').extract_first()

        data = {
            'player': title,
            'gamelog': []
        }

        for row in rows:
            data['gamelog'].append({
                'minutes': row.xpath('td[@data-stat="mp"]/text()').extract_first(),
                'date': row.xpath('td[@data-stat="date_game"]/a/text()').extract_first(),
                'fta': row.xpath('td[@data-stat="fta"]/text()').extract_first()
            })
        yield data
