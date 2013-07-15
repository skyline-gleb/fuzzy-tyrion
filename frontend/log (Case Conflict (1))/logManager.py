import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

class logManager:
    __addr = ""
    __logErrors = []
    __logJUNIT = []
    suteName  = ""
    timestamp = 0
    host = ""
    def printLog(self):
        for item in self.__logErrors:
            print item
    def __init__(self, address = ""):
        if address == "":
            return
        self.__addr = address
    def addPathJUNIT(self, address = ""):
        if address == "":
            return
        self.__addr = address
    def addLog(self, element):
        self.__logErrors.append(element)
        self.__logJUNIT.append(element)
    def __seveJUNIT(self, tree):
        root = tree.getroot()
        sute = ET.SubElement(root, "testsuite")
        sute.set( "name",self.suteName )
        sute.set( "host",self.host )
        sute.set( "timestamp",self.suteName )
        for itemLog in self.__logJUNIT:
            case = ET.SubElement(sute,"testcase")
            case.set("status",str(itemLog["status"]));
            case.set("time",str(itemLog["time"]))
            case.set("name",str(itemLog["name"]))
            error = ET.SubElement(case,"error")
            error.set("message",str(itemLog["message"]))
            del itemLog
        try:
            tree.write(self.__addr)
        except:
            return False
        return True
    def createReport(self):
        if self.__addr == "":
            return False
        tree = ElementTree()
        root = ET.Element("testsuites")
        tree._setroot(root)
        return self.__seveJUNIT(tree)
    def appendReport(self):
        if self.__addr == "":
            return False
        tree = ElementTree()
        try:
            tree.parse(self.__addr)
        except IOError:
            tree = ElementTree()
            root = ET.Element("testsuites")
            tree._setroot(root)
        return self.__seveJUNIT(tree)
    """def __del__(self):
        self.appendReport()"""
