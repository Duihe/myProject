#programmed by TaehuaGang

class Database:
    def __init__(self):
        self.dict = {}
     
    #1    
    def registNewCustomer(self, givenId, givenName):
        if givenId in self.dict: 
            return -1
        else:
            self.dict[givenId] = givenName 
                                        
            newdict ={}
            newdict[givenId] = givenName
                                        
            return newdict
            
    #2
    def getCustomerNumber(self):
        return int(self.dict.__len__())
    
    #3
    def getCustomerNameByID(self, givenId):
        returnDict = {}
        if givenId in self.dict:
            returnDict[givenId] = self.dict[givenId]
            return returnDict
        else:
            return -1
    #4 
    def getCustomerIDByName(self, givenName):
        allDict = {}
        if givenName in self.dict.values():
            for item in self.dict:
                if self.dict[item] == givenName:
                    allDict[item] = givenName
            return allDict
        else:
            return -1
    
    #5
    def getAllCustomer(self):
        return self.dict
    
    #6
    def removeCustomerByID(self, givenId):
        if givenId in self.dict:
            del self.dict[givenId] 
            return self.dict
        else:
            return -1
    
    
    #7 
                     
    def removeCustomerByName(self, givenName):
        keys_to_delete = [] 
        if givenName in self.dict.values():
            for key in self.dict:
                if self.dict[key] == givenName:
                    keys_to_delete.append(key)
            for key in keys_to_delete:
                del self.dict[key]  
            return self.dict 
        else:
            return -1


    
    #8
    def getAllCustomerNameSorted(self):
        nameDict = self.dict.values()
        return sorted(set(nameDict)) 
    
    #9
    def getAllCustomerIDSorted(self):
        idDict = []
        for id in self.dict:
            idDict.append(id)
        return sorted(idDict)

    #10 
    def getDuplicatedCustomerNames(self):
        reList = []
        middleList = []
        reDict = {}
        for item in self.dict.values():
            reList.append(item)
        for value in reList:
            if reList.count(value) >= 2:
                middleList.append(value)
        for key in self.dict:
            if self.dict[key] in middleList:
                reDict[key] = self.dict[key]
        return reDict
