from frontend.config.configvalidator import Check
import unittest
import json

class TestCheck(unittest.TestCase):

    def setUp(self):
        self.count_e = 1
        filename_e = []
        filename_e.append("frontend/tests/config/testconfig1.json")
        self.testdict_e = {0:{}}

        self.count_f = 2
        filename_f = []
        filename_f.append("frontend/tests/config/testconfig_f1.json")
        filename_f.append("frontend/tests/config/testconfig_f2.json")
        self.testdict_f = {0:{}}

        for i in range(0,self.count_e):
            with open(filename_e[i], 'rt') as config_file:
                self.testdict_e[i] = json.loads(config_file.read())

        for i in range(0,self.count_f):
            with open(filename_f[i], 'rt') as config_file:
                self.testdict_f[i] = json.loads(config_file.read())

        """with open(filename, 'rt') as config_file1:
            self.testdict_f1 = json.loads(config_file1.read())"""

    def testRunE(self):
        for i in range(0,self.count_e):
            obj = Check(self.testdict_e[i])
            self.assertEqual(obj.Run(),1)

    def testRunF(self):
        for i in range(0,self.count_f):
            obj1 = Check(self.testdict_f[i])
            self.assertFalse(obj1.Run() == 1)


if __name__ == "__main__":
    unittest.main()
