import unittest
import os
from frontend.log.logManager import LogManager

class TestLogManager(unittest.TestCase):
    def setUp(self):
        self.log = LogManager("2.xml","1.txt")
        self.log.addLog({"status":501, "message":"SsssS1", "name":"config1"})
        self.log.addLog({"status":502, "message":"SsssS2", "name":"config2"})
        
    def testCreateReport( self ):
        self.log.createReport()
        f = open("2.xml")
        m = f.read()
        self.assertNotEqual(m,"")

    def testCreateLog( self ):
        self.log.createLog()
        f = open("1.txt")
        m = f.read()
        self.assertNotEqual(m,"")
    def tearDown( self ):
        del self.log
        try:
            os.remove("2.xml")
            os.remove("1.txt")
        except:
            return
        
