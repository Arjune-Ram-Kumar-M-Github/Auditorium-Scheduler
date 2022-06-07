from Event import Event

class Month:
    def __init__(self,name,noOfDays):
        self.name = name
        self.noOfDays = noOfDays
        self.days = [None]*(noOfDays+1)

    def dayOfWeek(self,d, m, y):
        t = [ 0, 3, 2, 5, 0, 3,
            5, 1, 4, 6, 2, 4 ]
        y -= m < 3
        return (( y + int(y / 4) - int(y / 100)
                + int(y / 400) + t[m - 1] + d) % 7)
 
    def getDay(self,dayId):
        day = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
        return day[dayId]

    def findNewDate(self,fromDay):
        for day in range(fromDay+1,self.noOfDays+1):
            if self.days[day] == None:
                return day

        return -1

    def setEvent(self,day,eventName,eventTime,description):
        if self.days[day] == None:
            self.days[day] = Event(eventName,eventTime,description)
            return True
        else:
            return False
        
    def getEvent(self,day):
        return self.days[day] if self.days[day] != None else -1

    def deleteEvent(self,day):
        self.days[day] = None