import datetime


class DateClass:
    def __init__(self, counNum):
        self.counNum = counNum
        self.now = datetime.datetime.now()
        self.current_year = datetime.datetime.now().year

    def getDobFromAge(self) -> int:
        dob = self.current_year - self.counNum
        return dob
