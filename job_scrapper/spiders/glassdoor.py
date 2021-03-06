# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from job_scrapper.items import JobItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class GlassdoorSpider(scrapy.Spider):
    name = 'glassdoor'
    allowed_domains = []
    start_urls = ['https://www.glassdoor.com/Job/software-engineer-jobs-SRCH_KO0,17.htm']
    page = 0

    def parse(self, response):
        print("Start!!!!!!!!!!!!!!!!!!")
        job_list = response.css('.jl')

        for job in job_list:
            #print("FOUND!")
            jobItem = JobItem()
            detail_url = job.css('.logoWrap a::attr(href)').extract_first()
            title = job.css('.flexbox .jobLink::text').extract_first()
            location = job.css('.flexbox .subtle::text').extract_first()

            jobID = detail_url.split("=")[-1]
            #print(jobID)
            jobItem['jobID'] = jobID
            jobItem['title'] = title
            jobItem['location'] = location
            #print(title)
            url = 'https://www.glassdoor.com'+detail_url
            #print(url)
            request = scrapy.Request(url=url, callback=self.read_jobs, meta=dict(jobItem=jobItem))
            yield request

        # global page
        # page = page + 1
        # if page < 20:
        next = response.css('.next a::attr(href)').extract_first()
        next_url = 'https://www.glassdoor.com'+next
        yield scrapy.Request(url=next_url, callback=self.parse)



    def read_jobs(self, response):
        print("$$$$$$$$$$START$$$$$$$$$$$$$")

        jobItem = response.meta['jobItem']

        company_name = response.xpath('//*[@id="HeroHeaderModule"]/div[3]/div[2]/span[1]/text()').extract_first()
        #location = response.css('#HeroHeaderModule > div.empInfo.tbl > div.header.cell.info > span.subtle.ib::text').extract_first()

        sel = response.css('#JobDescContainer > div.jobDescriptionContent.desc')
        details = sel.xpath('//*[@id="JobDescContainer"]/div[1]/ul[1]//text()').extract()
        details + sel.xpath('//*[@id="JobDescContainer"]/div[1]/ul[2]//text()').extract()

        jobItem['company_name'] = company_name

        jobItem['details'] = details

        yield jobItem

    # def errback_httpbin(self, failure):
    #     print("$$$$$$$$$$START$$$$$$$$$$$$$")
    #     self.logger.error(repr(failure))
    #
    #     if failure.check(HttpError):
    #         # these exceptions come from HttpError spider middleware
    #         # you can get the non-200 response
    #         response = failure.value.response
    #         self.logger.error('HttpError on %s', response.url)
    #
    #     elif failure.check(DNSLookupError):
    #         # this is the original request
    #         request = failure.request
    #         self.logger.error('DNSLookupError on %s', request.url)
    #
    #     elif failure.check(TimeoutError, TCPTimedOutError):
    #         request = failure.request
    #         self.logger.error('TimeoutError on %s', request.url)

