import scrapy

# inherit from the spider class


class NewsSpider(scrapy.Spider):
    #name is required
    name = 'news'

    # start urls (list)
    start_urls = ['https://www.wiwi.uni-frankfurt.de/en/news-archiv.html']

    # parsing function
    def parse(self, response):
        for news in response.css('.contentcol-content .news-list-view .article'):

            yield {
                'name': news.css('h3 a::text').get(),
                'date': news.css('.news-list-date::text').get(),
                'teaser': news.css('.teaser-text p::text').get()
            }

        next_page = response.css(
            '.browseLinksWrap a:nth-last-child(2)').attrib['href']
        if next_page is not None:
            # follow if not none, and callback parse function
            yield response.follow(next_page, callback=self.parse)
