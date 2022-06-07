from Month import Month

class Calender:
    def __init__(self,year):
        self.year = year
        self.months = [None]*13
        self.monMap = {1 : 'January',2 : 'February',3 :' March',4 :'April',5 : 'May',6 : 'June',7 : 'July',8 : 'August',9 : 'September',10 : 'October',11 : 'November',12 : 'December'}

        self.generateMonths()

    def generateMonths(self):
        for monId in range(1,13):
            self.months[monId] = Month(self.getMonthName(monId),self.getNoofDays(monId))

    def getMonthName(self,monId):
        return self.monMap[monId]
    
    def getNoofDays(self,monId):
        if monId == 2:
            if self.year%4 == 0 and self.year%400 == 0:
                return 29
            else:
                return 28

        else:
            if monId%2 == 0:
                return 30
            else:
                return 31

    def getMonth(self,monId )-> Month:
        return self.months[monId]



