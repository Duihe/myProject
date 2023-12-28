#programmed by TaehuaGang

class Time:
    def __init__(self, hour, minu, sec):
        if hour < 24:
            self.hour = hour
        else:
            self.hour = 0
        if minu < 60:
            self.minu = minu
        else:
            self.minu = 0
        if sec < 60:
            self.sec = sec
        else:
            self.sec = 0
            
    def getTimeTuple(self):
        return (self.hour, self.minu, self.sec)
    

    def getTimeString(self):
        reH = ""
        reM = ""
        reS = ""
        if self.hour < 10:
            reH = "0"+str(self.hour)
        else:
            reH = str(self.hour)
        if self.minu < 10:
            reM = "0"+str(self.minu)
        else:
            reM = str(self.minu)
        if self.sec < 10:
            reS = "0"+str(self.sec)
        else:
            reS = str(self.sec)
        reA =  "{}:{}:{}".format(reH, reM, reS)
        return reA
    
class Time_24_View(Time):
    def __init__(self, hour, minu, sec):
        super().__init__(hour, minu, sec)
    
    def getViewString(self):
        reH = ""
        reM = ""
        reS = ""
        if self.hour < 10:
            reH = "0"+str(self.hour)
        else:
            reH = str(self.hour)
        if self.minu < 10:
            reM = "0"+str(self.minu)
        else:
            reM = str(self.minu)
        if self.sec < 10:
            reS = "0"+str(self.sec)
        else:
            reS = str(self.sec)
        reA = "{}:{}:{}".format(reH, reM, reS)
        return reA
    
    def __str__(self):
        reH = ""
        reM = ""
        reS = ""
        if self.hour < 10:
            reH = "0"+str(self.hour)
        else:
            reH = str(self.hour)
        if self.minu < 10:
            reM = "0"+str(self.minu)
        else:
            reM = str(self.minu)
        if self.sec < 10:
            reS = "0"+str(self.sec)
        else:
            reS = str(self.sec)
        reA = "{}:{}:{}".format(reH, reM, reS)
        return reA
    
    
class Time_12_View(Time):
    def __init__(self, hour, minu, sec):
        super().__init__(hour, minu, sec)
    
    def getViewString(self):
        reH = ""
        reM = ""
        reS = ""
        reT = ""
        if self.hour < 10:
            reH = "0"+str(self.hour)
        else:
            reH = str(self.hour)
        if self.minu < 10:
            reM = "0"+str(self.minu)
        else:
            reM = str(self.minu)
        if self.sec < 10: 
            reS = "0"+str(self.sec)
        else:
            reS = str(self.sec)
        if self.hour >=12:
            reT = "PM"
        else:
            reT = "AM"
        reA = "{}:{}:{} {}".format(reH, reM, reS, reT)
        return reA
        
    def __str__(self):
        reH = ""
        reM = ""
        reS = ""
        reT = ""
        if self.hour < 10:
            reH = "0"+str(self.hour)
        else:
            reH = str(self.hour)
        if self.minu < 10:
            reM = "0"+str(self.minu)
        else:
            reM = str(self.minu)
        if self.sec < 10:
            reS = "0"+str(self.sec)
        else:
            reS = str(self.sec)
        if self.hour >=12:
            reT = "PM"
        else:
            reT = "AM"
        reA = "{}:{}:{} {}".format(reH, reM, reS, reT)
        return reA
        
class Clock:
    def __init__(self, objectTime):
        if type(objectTime) != Time_12_View and type(objectTime) != Time_24_View:
            self.view = Time_24_View(0,0,0)
            self.alarm = []
        else:
            self.view = objectTime
            self.alarm = []
    
    def getClockTime(self):
        if type(self.view) == Time_24_View: 
            reH = ""
            reM = ""
            reS = ""
            if self.view.hour < 10:
                reH = "0"+str(self.view.hour)
            else:
                reH = str(self.view.hour)
            if self.view.minu < 10:
                reM = "0"+str(self.view.minu)
            else:
                reM = str(self.view.minu)
            if self.view.sec < 10:
                reS = "0"+str(self.view.sec)
            else:
                reS = str(self.view.sec)
            reA = "{}:{}:{}".format(reH, reM, reS)
            return reA 
        if type(self.view) == Time_12_View:
            reH = ""
            reM = ""
            reS = ""
            reT = ""
            if self.view.hour < 10:
                reH = "0"+str(self.view.hour)
            else:
                reH = str(self.view.hour)
            if self.view.minu < 10:
                reM = "0"+str(self.view.minu)
            else:
                reM = str(self.view.minu)
            if self.view.sec < 10:
                reS = "0"+str(self.view.sec)
            else:
                reS = str(self.view.sec)
            if self.view.hour >=12:
                reT = "PM"
            else:
                reT = "AM"
            reA = "{}:{}:{} {}".format(reH, reM, reS, reT)
            return reA
        
    def changeClockTimeMode(self):
        if type(self.view) == Time_12_View:
            self.view = Time_24_View(self.view.hour, self.view.minu, self.view.sec)
            reH = ""
            reM = ""
            reS = ""
            if self.view.hour < 10:
                reH = "0"+str(self.view.hour)
            else:
                reH = str(self.view.hour)
            if self.view.minu < 10:
                reM = "0"+str(self.view.minu)
            else:
                reM = str(self.view.minu)
            if self.view.sec < 10:
                reS = "0"+str(self.view.sec)
            else:
                reS = str(self.view.sec)
            reA = "{}:{}:{}".format(reH, reM, reS)
            return reA 
        if type(self.view) == Time_24_View:
            self.view = Time_12_View(self.view.hour, self.view.minu, self.view.sec)
            reH = ""
            reM = ""
            reS = ""
            reT = ""
            if self.view.hour < 10:
                reH = "0"+str(self.view.hour)
            else:
                reH = str(self.view.hour)
            if self.view.minu < 10:
                reM = "0"+str(self.view.minu)
            else:
                reM = str(self.view.minu)
            if self.view.sec < 10:
                reS = "0"+str(self.view.sec)
            else:
                reS = str(self.view.sec)
            if self.view.hour >=12:
                reT = "PM"
            else:
                reT = "AM"
            reA = "{}:{}:{} {}".format(reH, reM, reS, reT)
            return reA
    
    def setClockTime(self, object2):
        if "AM" in object2 or "PM" in object2:
            object2 = Time_12_View(int(object2[0:2])), int(object2[3:5]), int(object2[6:8]) 
            self.view = object2
        else:
            object2 = Time_24_View(int(object2[0:2])), int(object2[3:5]), int(object2[6:8]) 
            self.view = object2
        if type(self.view) == Time_24_View:
            reH = ""
            reM = ""
            reS = ""
            if self.view.hour < 10:
                reH = "0"+str(self.view.hour)
            else:
                reH = str(self.view.hour)
            if self.view.minu < 10:
                reM = "0"+str(self.view.minu)
            else:
                reM = str(self.view.minu)
            if self.view.sec < 10:
                reS = "0"+str(self.view.sec)
            else:
                reS = str(self.view.sec)
            reA = "{}:{}:{}".format(reH, reM, reS)
            return reA 
        if type(self.view) == Time_12_View:
            reH = ""
            reM = ""
            reS = ""
            reT = ""
            if self.view.hour < 10:
                reH = "0"+str(self.view.hour)
            else:
                reH = str(self.view.hour)
            if self.view.minu < 10:
                reM = "0"+str(self.view.minu)
            else:
                reM = str(self.view.minu)
            if self.view.sec < 10:
                reS = "0"+str(self.view.sec)
            else:
                reS = str(self.view.sec)
            if self.view.hour >=12:
                reT = "PM"
            else:
                reT = "AM"
            reA = "{}:{}:{} {}".format(reH, reM, reS, reT)
            return reA
    
    def addAlarm(self, object3):
        if type(object3) == Time_12_View or type(object3) == Time_24_View:
            self.alarm.append(object3)
        return len(self.alarm)
    
    
    def getAlarmRemainsInSecondList(self):
        alarmSec = [] 
        nH = int(str(self.view[0:2]))
        nM = int(str(self.view[3:5]))
        nS = int(str(self.view[6:8]))
        nSec += nH * 3600
        nSec += nM * 60
        nSec += nS
    
        if len(self.alarm) >= 2:
            for i in range(0,len(self.alarm)):
                calcSec = 0
                alH = int(str(self.alarm[i][0:2]))
                alM = int(str(self.alarm[i][3:5]))
                alS = int(str(self.alarm[i][6:8]))
                calcSec += alH * 3600
                calcSec += alM * 60
                calcSec += alS
                if nSec > calcSec:
                    calcSec += 3600*24
                alarmSec.append(nSec-calcSec)
        else:
            calcSec = 0
            alH = int(str(self.alarm[0][0:2]))
            alM = int(str(self.alarm[0][3:5]))
            alS = int(str(self.alarm[0][6:8]))
            calcSec += alH * 3600
            calcSec += alM * 60
            calcSec += alS
            if nSec > calcSec:
                calcSec += 3600*24
            alarmSec.append(nSec-calcSec)
        return alarmSec
        
        