import sys
import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

class LogManager:
    __addr = ""
    __addrLog = ""
    __logErrors = []
    __logJUNIT = []
    __logFile = []
    __arStatus = ["Informational","Success","Redirection","Client Error","Server Error"]
    suteName  = "Test 2gis"
    timestamp = 0
    host = "api.2gis.ru"
    def __init__(self, address = "", addressLog = ""):
        if address == "":
            return
        self.__addr = address
        if addressLog == "":
            return
        self.__addrLog = addressLog
        self.timestamp = time.time()
    def addPathJUNIT(self, address = ""):
        if address == "":
            return
        self.__addr = address

    def addPathLog(self, address):
        if address:
            self.__addrErrors = address
            
    def addLog(self, element):
        element["status_area"] = int(element["status"] / 100 )
        element["status_area_text"] = self.__arStatus[element["status_area"] -1]
        element["time"] = time.time()
        self.__logErrors.append(element)
        self.__logJUNIT.append(element)
        self.__logFile.append(element)
        return self.__logErrors
 
    def __seveJUNIT(self, tree):
        root = tree.getroot()
        sute = ET.SubElement(root, "testsuite")
        sute.set( "name",self.suteName )
        sute.set( "host",self.host )
        sute.set( "timestamp",str(self.timestamp) )
        for itemLog in self.__logJUNIT:
            if itemLog["status_area"] != 5:
                continue
            case = ET.SubElement(sute,"testcase")
            case.set("status",str(itemLog["status"]));
            case.set("time",str(itemLog["time"]))
            case.set("name",str(itemLog["name"]))
            error = ET.SubElement(case,"error")
            error.set("message",str(itemLog["message"]))
            error.set("type",str(itemLog["status_area_text"]))
            del itemLog
        try:
            tree.write(self.__addr)
        except:
            return False
        return True
    def __createString( self, item ):
        return item["status_area_text"] + " " + str(item["status"]) + ": " + item["name"] + " " + item["message"] + "\n"

    def printLog(self):
        print(self.__createString( self.__logErrors[-1] ))
    def printAllLogs(self):
        for item in self.__logErrors:
            print(self.__createString( item ))
            
    def __seveLogFile(self, file):
        s = ""
        for itemLog in self.__logFile:
            s = s + self.__createString( itemLog )
            del itemLog
        file.write(s)
        file.close()
        
    def createLog(self):
        if self.__addrLog == "":
            return False
        file = open(self.__addrLog,'w')
        return self.__seveLogFile( file )

    def appendLog(self):
        if self.__addrLog == "":
            return False
        file = open(self.__addrLog,'a')
        return self.__seveLogFile( file )
        
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
