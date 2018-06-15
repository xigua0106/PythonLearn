from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

# 异常处理
def ErrorHandler(self, failure):
    self.logger.error(repr(failure))

    if failure.check(HttpError):
        response = failure.value.response
        self.logger.error('HttpError on %s', response.url)

    elif failure.check(DNSLookupError):
        request = failure.request
        self.logger.error('DNSLookupError on %s', request.url)

    elif failure.check(TimeoutError, TCPTimedOutError):
        request = failure.request
        self.logger.error('TimeoutError on %s', request.url)
    else:
        self.logger.error(failure.request.url)