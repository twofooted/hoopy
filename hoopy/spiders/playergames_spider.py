import time
import scrapy

class PlayerGameSpider(scrapy.Spider):
    name = "playergames"

    start_urls = [
        'https://www.basketball-reference.com/players/a/',
    ]

    def parse(self, response):
        
    
        self.player = response.xpath('//table[@id="players"]/tbody/tr/th/a/text()').extract()

        next_url = response.xpath('//table[@id="players"]/tbody/tr/th/a/@href').extract()
        
        yield response.follow(next_url, callback=self.parse_player_page)
        

    def parse_player_page(self, response):
        gamelog_urls = response.xpath('//tbody/tr/th/a/@href').extract()

        for url in gamelog_urls:
            time.sleep(5)
            yield response.follow(url, callback=self.parse_stats)
    
    def parse_stats(self, response):

        rows = response.xpath('//table[@id="pgl_basic"]/tbody/tr')

        for row in rows:
            date_game = row.xpath('td[@data-stat="date_game"]/a/text()').extract_first()

            if date_game:

                yield {
                    'player': self.player,
                    'minutes': row.xpath('td[@data-stat="mp"]/text()').extract_first(),
                    'date': date_game,
                    'fta': row.xpath('td[@data-stat="fta"]/text()').extract_first()
                }
