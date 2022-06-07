from Calender import Calender        

class Scheduler:
    def __init__(self,year):
        self.year = year
        self.calender = Calender(year)

    def scheduleEvent(self,date,event):
        day,mon,yr = map(int,date.split("."))
        monObj = self.calender.getMonth(mon)
        eventName,eventTime,description = event

        if monObj.setEvent(day,eventName,eventTime,description):
            return
        else:
            self.findAvailability(date)

    def reScheduleEvent(self,fromDate,toDate):
        event = self.getEvent(fromDate,False)
        self.deleteEventFromSchedule(fromDate)
        self.scheduleEvent(toDate,[event.getName(),event.getTime(),event.getDescription()])

    def deleteEventFromSchedule(self,date):
        day,mon,yr = map(int,date.split("."))
        monObj = self.calender.getMonth(mon)
        monObj.deleteEvent(day)
        
    def findAvailability(self,date):
        day,mon,yr = map(int,date.split("."))
        monObj = self.calender.getMonth(mon)
        newDay = monObj.findNewDate(day)

        if newDay != -1:
            print("{}.{}.{} ({}) is Free".format(newDay,mon,yr,monObj.getDay(monObj.dayOfWeek(newDay,mon,yr))))
        else:
            print("No Slots available in this Month")

    def getEvent(self,date,flag = True):
        day,mon,yr = map(int,date.split("."))
        monObj = self.calender.getMonth(mon)
        ret = monObj.getEvent(day)
        if flag == True:
            ret.printEvent() if ret != -1 else print("No Event Scheduled")

        # if ret == -1:
        #     print("No Event Scheduled")

        return ret



