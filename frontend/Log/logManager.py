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
log = CLogManager("1.xml")
log.suteName = "Test sute"
log.timestamp = "3556565656"
log.host = "api.2gis.ru"

log.addLog({ "status":501, "time":56568982, "name":"Test Log", "message":"Is so gooood=))" })
log.addLog({ "status":504, "time":55656548, "name":"Test Log", "message":"Is so bad=(" })
log.addLog({ "status":503, "time":98921125, "name":"Test Log", "message":"Is bad=(" })
log.printLog()
log.appendReport()
