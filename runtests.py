#!/usr/bin/env python3

from frontend.tests import FuzzerTestCase
from frontend.tests.testLogManager import TestLogManager
from frontend.tests.config import TestCheck
import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FuzzerTestCase))
    suite.addTest(unittest.makeSuite(TestCheck))
    suite.addTest(unittest.makeSuite(TestLogManager))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)

