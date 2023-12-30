class MyClass:
    objectCount = 0 
    def __init__(self,givenId):
        self.id = givenId 
        MyClass.objectCount = MyClass.objectCount + 1  
        self.wordDict = {} 
    
    #1
    def getId(self):
        return self.id
    
    #2
    def setId(self, givenId):
        if type(givenId) == type(1.0) or type(givenId) == type(1): 
            self.id = "XXXX"
        else:
            self.id = givenId
            
    #3
    def getNumberOfObject(self): 
        return MyClass.objectCount
    
    #4
    def storeWordlistAsDictionary(self, givenWordList):
        givenWordList.sort()
        for i in givenWordList: 
            if i in self.wordDict:
                self.wordDict[i] = self.wordDict[i] + 1
            else:
                self.wordDict[i] = 1            
        return self.wordDict
    
    #5 
    def getWordCount(self, givenString):
        if givenString in self.wordDict.keys():
            return (givenString, self.wordDict[givenString])
        else:
            return False
            
    #6 
    def getWordList(self):
        if self.wordDict.__len__() != 0:
            dictKeys = []
            for item in self.wordDict:
                dictKeys.append(item)
            dictKeys.sort()
            return dictKeys
        else:
            return False
        
#7 
class MyDerivedClass(MyClass):
    def __str__(self):
        dictkeys = list(self.wordDict.keys()) 
        if dictkeys:  
           keys_string = ",".join(dictkeys) 
           return "<{}>".format(keys_string)
        else:
           return "<>"

        
    #8 
    def __gt__(self, object1):
        dictKeys = self.wordDict.keys() 
        dictBigyo = object1.wordDict.keys()
        if dictKeys.__len__() > dictBigyo.__len__():
            return True
        else:
            return False
        
    #9
    def __add__(self, givenList):
        finalReturnDict = MyDerivedClass()
        for (key,value) in givenList.wordDict.items(): 
            if key in self.wordDict:
                finalReturnDict.wordDict[key] = self.wordDict[key] + givenList.wordDict[key] 
            else:
                finalReturnDict.wordDict[key] = givenList.wordDict[key]  
        for (key, value) in self.wordDict.items(): 
            if key in finalReturnDict.wordDict:
                "none"
            else:
                finalReturnDict.wordDict[key] = self.wordDict[key]
        return finalReturnDict 
    
    #10 
    def __init__(self, givenId="****"):
        super().__init__(givenId) 
        