from r1080.items import R1080Item
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
from urlparse import urljoin

class R1080Spider(Spider):

    name = "r1080"

    allowed_domains = ["1080recetas.com"]

    start_urls = [
        "http://www.1080recetas.com/recetas",
    ]

    def parse(self, response):
        
        sel = Selector(response)

        selectors = sel.xpath("//*[@class='contentpagetitle']")

        r1080ItemList = []        

        for selector in selectors:

            text = selector.xpath("text()").extract()[0].strip()
            link = selector.xpath("@href").extract()[0].strip()

            yield Request(urljoin(response.url,link), callback=self.parse_job)

    def parse_job(self, response):

        r1080Item = R1080Item()

        sel = Selector(response)

        selector = sel.xpath("//*[@class='contentpagetitle']")[0]
        title = selector.xpath("text()").extract()[0].strip()
        r1080Item['title'] = title

        selector = sel.xpath("//*[@class='createdate']")[0]
        createdate = selector.xpath("text()").extract()[0].strip()
        r1080Item['createdate'] = createdate

        ingredients = []
        selectors = sel.xpath("//*[@class='article-content']/ul/li")
        for selector in selectors:
            ingredient = selector.xpath("text()").extract()[0].strip()
            ingredients.append ( ingredient )
        r1080Item['ingredients'] =  ingredients

        steps = []
        selectors = sel.xpath("//*[@class='article-content']/ol/li")
        for selector in selectors:
            step = selector.xpath("text()").extract()[0].strip()
            steps.append ( step )
        r1080Item['steps'] =  steps

        return r1080Item







