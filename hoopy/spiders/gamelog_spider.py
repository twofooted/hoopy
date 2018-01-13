import scrapy

class GameSpider(scrapy.Spider):
    name = "gamelog"

    start_urls = [
        'https://www.basketball-reference.com/players/a/',
        'https://www.basketball-reference.com/players/b/',
        'https://www.basketball-reference.com/players/c/',
        'https://www.basketball-reference.com/players/d/',
        'https://www.basketball-reference.com/players/e/',
        'https://www.basketball-reference.com/players/f/',
        'https://www.basketball-reference.com/players/g/',
        'https://www.basketball-reference.com/players/h/',
        'https://www.basketball-reference.com/players/i/',
        'https://www.basketball-reference.com/players/j/',
        'https://www.basketball-reference.com/players/k/',
        'https://www.basketball-reference.com/players/l/',
        'https://www.basketball-reference.com/players/m/',
        'https://www.basketball-reference.com/players/n/',
        'https://www.basketball-reference.com/players/o/',
        'https://www.basketball-reference.com/players/p/',
        'https://www.basketball-reference.com/players/q/',
        'https://www.basketball-reference.com/players/r/',
        'https://www.basketball-reference.com/players/s/',
        'https://www.basketball-reference.com/players/t/',
        'https://www.basketball-reference.com/players/u/',
        'https://www.basketball-reference.com/players/v/',
        'https://www.basketball-reference.com/players/w/',
        'https://www.basketball-reference.com/players/y/',
        'https://www.basketball-reference.com/players/z/',
    ]

    def parse(self, response):
        
        for row in response.xpath('//table[@id="players"]/tbody/tr'):
            player = row.xpath('th//a/text()').extract_first()
            year_min = row.xpath('td[@data-stat="year_min"]/text()').extract_first()
            year_max = row.xpath('td[@data-stat="year_max"]/text()').extract_first()
            pos = row.xpath('td[@data-stat="pos"]/text()').extract_first()
            birth_date = row.xpath('td[@data-stat="birth_date"]/a/text()').extract_first()
            college = row.xpath('td[@data-stat="college_name"]/a/text()').extract_first()

            yield {
                'player': player,
                'year_min': year_min,
                'year_max': year_max,
                'pos': pos,
                'birth_date': birth_date,
                'college': college
            }
        next_page = response.xpath('//table[@id="players"]/tbody/tr/th//a/@href').extract_first()
