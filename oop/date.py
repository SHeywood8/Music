class Date():
    def __init__(self, year : int, month = None, day = None):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        string = str(self.year)
        if self.month != None:
            string += '-' + str(self.month)
        if self.day != None:
            string += '-' + str(self.day)
        return string

    def get_year(self):
        return self.year