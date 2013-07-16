import json
import codecs

class Check:
    def __init__(self,temp):
        self.dictone = temp
        self.count1 = 5
        self.checkdict = {0:{"name": "api_url","type": str}}
        self.checkdict[1] = {"name": "rps","type": int}
        self.checkdict[2] = {"name": "headers","type": dict}
        self.checkdict[3] = {"name": "parameters","type": dict}
        self.checkdict[4] = {"name": "methods","type": dict}
        self.count2 = 3
        self.checkmethods = {0:{"name": "http_method", "type": str}}
        self.checkmethods[1] = {"name": "count", "type": int}
        self.checkmethods[2] = {"name": "parameters", "type": dict}
        self.count3 = 4
        self.checkparameters = {0:{"name": "required", "type": bool}}
        self.checkparameters[1] = {"name": "data_type", "type": str}
        self.checkparameters[2] = {"name": "value", "type": str}
        self.checkparameters[3] = {"name": "action", "type": str}        
    def Run(self):
        line = self.dictone.keys()
        i=0
        while i<self.count1:
            value = self.dictone.get(self.checkdict[i]["name"],-1)
            if value == -1:
                print("Error key level_1\nNot found:")
                print(self.checkdict[i]["name"])
                return -1
            else:
                if type(value) != self.checkdict[i]["type"]:
                    print("Error value level_1")
                    print(type(value))
                    print(value)
                    print(self.checkdict[i]["type"])
                    return -1
            i=i+1
        line = self.dictone["methods"].keys()
        for element in line:
            i=0
            while i<self.count2:
                value = self.dictone["methods"][element].get(self.checkmethods[i]["name"],-1)
                if value == -1:
                    print("Error key level_2\nNot found:")
                    print(self.checkmethods[i]["name"])
                    return -1
                else:
                    if type(value) != self.checkmethods[i]["type"]:
                        print("Error value level_2")
                        print(type(value))
                        print(value)
                        print(self.checkmethods[i]["type"])
                        return -1
                parameters = self.dictone["methods"][element]["parameters"].keys()
                for par_el in parameters:
                    j=0
                    while j<self.count3:
                        value = self.dictone["methods"][element]["parameters"][par_el].get(self.checkparameters[j]["name"],-1)
                        if value == -1:
                            print("Error key level_3\nNot found:")
                            print(self.checkparameters[j]["name"])
                            return -1
                        else:
                            if type(value) != self.checkparameters[j]["type"]:
                                print("Error value level_3")
                                print(type(value))
                                print(value)
                                print(self.checkparameters[i]["type"])
                                return -1
                        j=j+1
                        if j==2:
                            j=j+1
                i=i+1
        return 1
