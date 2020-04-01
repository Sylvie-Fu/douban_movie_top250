# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanmovieItem
import re


class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250?start=0&filter='
        yield scrapy.Request(url=url, headers=self.headers)


    def parse(self, response):
        movie_list = response.css('.grid_view li')
        for movie in movie_list:
            item = DoubanmovieItem()
            item['ranking'] = movie.css('.item .pic em::text').extract_first()
            item['title'] = [x.replace('\xa0/\xa0', '') for x in movie.css('.item .info .hd a span::text').extract()]
            info = movie.css('.item .info .bd p::text').extract()
            print(info[1])
            item['year'] = re.findall('([0-9].*)\s+/\s+.*?\s+/\s+.*?\n', info[1])[0].strip()
            director = re.findall('导演: ([A-Z\u4e00-\u9fa5·\-]* )?([šA-Za-z\u00C0-\u00FF \-\.]*)?', info[0])
            item['director'] = director[0] + director[1] if len(director) > 1 else director[0]
            item['region'] = re.findall('[0-9].*\s+/\s+(.*?)\s+/\s+.*?\n', info[1])[0].strip()
            item['category'] = re.findall('[0-9].*\s+/\s+.*?\s+/\s+(.*?)\n', info[1])[0].strip()
            rate = movie.css('.item .info .bd .star').extract_first()
            print(type(rate))
            item['rate'] = re.findall('([0-9]\.[0-9])', rate)[0]
            item['score_number'] = re.findall('([0-9]+)人评价', rate)[0]
            item['comment'] = movie.css('.item .info .bd .quote .inq::text').extract_first()

            yield item

        next = response.css('.paginator .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)


