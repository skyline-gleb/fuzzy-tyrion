from frontend import Fuzzer
import unittest


class FuzzerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fuzzer = Fuzzer('url')

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


if __name__ == '__main__':
    unittest.main()
