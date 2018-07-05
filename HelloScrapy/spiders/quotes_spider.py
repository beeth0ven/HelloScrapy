import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'file:///home/luojie/Documents/PyCharmProjects/HelloScrapy/HelloScrapy/spiders/pinterest.html'
        # yield {
        #     'image_urls': [],
        # }
        yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        # hrefs = response.xpath('//div[@class="box list channel"]/ul/li/a/@href').extract()
        # self.log('hrefs: %s' % hrefs)
        # for href in hrefs:
        #     yield response.follow(href, callback=self.parse_image_urls)
        image_urls = response.xpath('//img/@src').extract()
        self.log('image_urls count: %s' % len(image_urls))
        self.log('image_urls: %s' % image_urls)

        # url = 'https://i.pinimg.com/originals/b9/58/9d/b9589d851dc44f8c18f44dd056a9f379.jpg'
        # yield {
        #     'image_urls': image_urls,
        # }
            # yield scrapy.Request(url=url, callback=self.parse_image_urls)


    # def parse_image_urls(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # image_urls = response.xpath('//div[@class="pics"]/img/@src').extract()
        # self.log('image_urls: %s' % image_urls)
        # yield {
        #     'image_urls': image_urls,
        # }
