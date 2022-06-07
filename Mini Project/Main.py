from Scheduler import Scheduler

if __name__ == "__main__":
    choice = input("\nPress 1 to take input from text file\nPress 2 to take input from console: ")
    if choice == "1":
        file = open("input.txt","r").readlines()
        s = Scheduler(int(file[0].strip()))
        for line in file[1:]:
            func,*arg = line.strip().split(",")

            if func == "1":
                s.scheduleEvent(arg[0],arg[1].split(":"))
            elif func == "2":
                s.reScheduleEvent(arg[0],arg[1])
            elif func == "3":
                s.deleteEventFromSchedule(arg[0])
            elif func == "4":
                s.getEvent(arg[0])
    else:
        s = Scheduler(int(input("Enter the Scheduling Year: ")))

        while(True):
            inp = int(input("\nEnter 1 to Schedule Event\nEnter 2 to Reschedule a Event\nEnter 3 to Delete a Scheduled Event\nEnter 4 to Get Event Details\nEnter 5 to Exit: "))

            if inp == 1:
                date = input("\nEnter Date: ")
                event = list(input("\nEnter Event Details (Name,Time,Description): ").split(","))
                s.scheduleEvent(date,event)

            elif inp == 2:
                fromDate = input("\nEnter from Date: ")
                toDate = input("\nEnter to Date: ")
                s.reScheduleEvent(fromDate,toDate)
            
            elif inp == 3:
                date = input("\nEnter Date: ")
                s.deleteEventFromSchedule(date)
            
            elif inp == 4:
                date = input("\nEnter Date: ")      
                s.getEvent(date)

            elif inp == 5:
                break

