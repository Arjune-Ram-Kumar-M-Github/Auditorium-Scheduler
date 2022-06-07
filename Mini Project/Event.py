class Event:
    def __init__(self,name,time,description):
        self.name = name
        self.time = time
        self.description = description

    def getName(self):
        return self.name
    
    def getTime(self):
        return self.time

    def getDescription(self):
        return self.description

    def printEvent(self):
        print("Name: ",self.getName())
        print("Time: ",self.getTime())
        print("Description: ",self.getDescription())



