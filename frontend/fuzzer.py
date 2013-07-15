import re
import time
import random
from request import *
from log import *
from itertools import chain
from datagenerator import *
from gen import DataGenerator


class Fuzzer(object):
    def __init__(self, api_url, rps=10, headers={}, parameters={}):
        self.api_url    = api_url
        self.rps        = rps
        self.headers    = headers
        self.parameters = parameters

    def test_methods(self, methods):
        for api_method, options in methods.items():
            for index in range(options['count']):
                self.test_method(api_method, options['http_method'], options['parameters'])
                time.sleep(1.0 / self.rps)

    def test_method(self, api_method, http_method, parameters):
        data     = self.prepare_data(parameters)
        payload  = dict(chain(self.parameters.items(), data.items()))
        url      = self.make_url(self.api_url, api_method, payload)
        request  = self.make_request(http_method, url, payload, self.headers)
        response = request.send()
        self.log(response)

    def make_url(self, api_url, api_method, payload):
        return re.sub(r'{(.+?)}',
                      lambda m: str(payload[m.group(1)]) if m.group(1) in payload else m.group(0),
                      api_url + api_method)

    def make_request(self, http_method, url, payload, headers):
        request = Request(http_method, url)
        request.add_headers(headers)
        request.add_params(payload)
        return request

    def prepare_data(self, parameters):
        data = {}
        generator = DataGenerator()
        methods = [generator.getInteger32, generator.getString]
        for parameter, options in parameters.items():
            value = options['value']
            if options['action'] == 'mutate':
                if options['data_type'] == 'int':
                    value = generator.getInteger32()
                else:
                    value = generator.getString()
            elif options['action'] == 'generate':
                get_value = random.choice(methods)
                value = get_value()
            data[parameter] = value
        return data

    def log(self, response):
        if (response.error_msg == None):
            msg = response.request['method'] + ' ' + response.request['url'] + '\n'
            msg += str(response.status_code) + ' ' + response.status_msg + '\n'
            Log.write(msg)
        else:
            Log.write(response.error_msg)
