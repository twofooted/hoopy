import scrapy

class PlayerListSpider(scrapy.Spider):
    ''' Gets all NBA players listed on basketball-reference's site '''

    name = "playerlist"

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
        ''' main function for parsing the NBA player table for each page '''
        for row in response.xpath('//table[@id="players"]/tbody/tr'):
            player = row.xpath('th//a/text()').extract_first()
            if row.xpath('th[@data-stat="player"]/strong/a'):
                is_activte = True
            else:
                is_activte = False

            player_url = row.xpath('th[@data-stat="player"]//a/@href').extract_first()
            year_min = row.xpath('td[@data-stat="year_min"]/text()').extract_first()
            year_max = row.xpath('td[@data-stat="year_max"]/text()').extract_first()
            pos = row.xpath('td[@data-stat="pos"]/text()').extract_first()
            birth_date = row.xpath('td[@data-stat="birth_date"]/a/text()').extract_first()
            college = row.xpath('td[@data-stat="college_name"]/a/text()').extract_first()
            
            yield {
                'player': player,
                'start_year': year_min,
                'end_year': year_max,
                'position': pos,
                'birthdate': birth_date,
                'college': college,
                'is_active': is_activte,
                'url': player_url
            }
