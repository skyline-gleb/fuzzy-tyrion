#!/usr/bin/env python3

from frontend.tests import FuzzerTestCase
import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FuzzerTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)

