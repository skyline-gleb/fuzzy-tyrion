from frontend import Fuzzer
from frontend.http.request import Request
import unittest


class FuzzerTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.fuzzer = Fuzzer('http://api.localhost/v{version}/')

    def test_prepare_data_generate(self):
        parameters = {'where': {'action': 'generate', 'required': True, 'value': 'Novosibirsk', 'data_type': 'string'}}
        data = self.fuzzer.prepare_data(parameters)
        self.assertEqual(['where'], list(data.keys()))

    def test_prepare_data_mutate(self):
        parameters = {'where': {'action': 'mutate', 'required': True, 'value': 'Novosibirsk', 'data_type': 'string'},
                      "test": {"required": True, "data_type": "int", "value": "42", "action": "mutate"}}
        data = self.fuzzer.prepare_data(parameters)
        self.assertNotIsInstance(data['where'], int)
        self.assertIsInstance(data['test'], int)

    def test_make_url(self):
        expected_url = 'http://api.localhost/v1/categories/cat1/items/1234'
        api_method = 'categories/{category}/items/{item_id}'
        payload = {'version': '1', 'category': 'cat1', 'item_id': 1234}
        actual_url = self.fuzzer.make_url(self.fuzzer.api_url, api_method, payload)
        self.assertEqual(actual_url, expected_url)

    def test_make_request(self):
        http_method = 'GET'
        url = 'http://api.localhost/v1/users/1'
        payload = {'fields': 'username, email'}
        headers = {'Accept': 'application/json'}
        
        expected_request = Request(http_method, url)
        expected_request.add_headers(headers)
        expected_request.add_params(payload)

        actual_request = self.fuzzer.make_request(http_method, url, payload, headers)
        
        self.assertEqual(vars(actual_request), vars(expected_request))


if __name__ == '__main__':
    unittest.main()
