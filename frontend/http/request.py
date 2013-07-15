import requests
from response import *


class Request(object):

    def __init__(self, method, url):
        self.method  = method.upper()
        self.url     = url
        self.headers = {}
        self.data    = {}
        self.params  = {}
        self.timeout = 10

    def add_params(self, params):
        if self.method in ['POST', 'PUT', 'PATCH', 'TRACE']:
            self.data = params
        else:
            self.params = params

    def add_headers(self, headers):
        self.headers = headers

    def set_timeout(self, timeout):
        self.timeout = timeout

    def send(self):
        try:
            r = requests.request(self.method, self.url, headers=self.headers,
                                 params=self.params, data=self.data, timeout=self.timeout)

        except Exception as e:
            return Response(error_msg=str(e))

        request = {'method': self.method, 'url': r.request.url, 'body': r.request.body}
        return Response(request=request, status_code=r.status_code, status_msg=r.reason,
                        encoding=r.encoding, time=r.elapsed, content=r.text.encode(r.encoding))
