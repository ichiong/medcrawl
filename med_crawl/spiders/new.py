from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.utils.response import get_base_url
from med_crawl.items import MedCrawlItem

class MySpider(CrawlSpider):
    name = 'mcr'
    allowed_domains = ['321.portal.athenahealth.com']
    start_urls = ['https://6078.portal.athenahealth.com/']

    

    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sel = Selector(response)
        sites = hxs.select("//div[@id='loginpane']")
        items = []
        
        
        for site in sites:
            item = MedCrawlItem()
            item['title'] = hxs.select('//form[contains(@id, "email")]').extract()
            #item['link'] = site.xpath('//div[contains(@class, "login")]').extract()
            item['link'] = get_base_url(response)
            items.append(item)
        return items
