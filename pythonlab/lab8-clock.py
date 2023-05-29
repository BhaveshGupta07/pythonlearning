class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def display_time(self):
        print("Time:",self.hour,":",self.minute,":",self.second)

class Calendar:
    def __init__(self, month, date):
        self.month = month
        self.date = date

    def display_date(self):
        print("Date:",self.date,"-",self.month)

class CalendarClock(Calendar,Clock):
    def __init__(self, hour, minute, second, month, date):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, month, date)

    def display_calendar_clock(self):
        self.display_date()
        self.display_time()

cObj = CalendarClock(12, 30, 45, 5, 27) #object of the date 27-05 with time
cObj.display_calendar_clock()
