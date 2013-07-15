import requests
from response import *


class Request(object):

    def __init__(self, method, url, fields={}, headers={}, timeout=10):
        self.method = method.upper()
        self.url = url
        self.headers = headers
        self.timeout = timeout

        if method in ['POST', 'PUT', 'PATCH', 'TRACE']:
            self.data = fields
            self.params = {}
        else:
            self.data = {}
            self.params = fields

    def send(self):

        try:
            r = requests.request(self.method, self.url, headers=self.headers,
                                 params=self.params, data=self.data, timeout=self.timeout)

        except Exception as e:
            return Response(error_msg=str(e))

        request = {'method': self.method, 'url': r.request.url, 'body': r.request.body}
        return Response(request=request, status_code=r.status_code, status_msg=r.reason,
                        encoding=r.encoding, time=r.elapsed, content=r.text.encode(r.encoding))
