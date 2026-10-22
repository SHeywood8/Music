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

def str_to_date(date_str:str):
    err_str = "Incorrect date format, please use yyyy-mm-dd"
    if date_str == '':
        print(err_str)
        return None
    date_parts = date_str.split("-")
    if not len(date_parts[0]) == 4:
        print(err_str)
        return None
    date_obj = Date(date_parts[0])
    if len(date_parts) > 1:
        if not len(date_parts[1]) == 2:
            print(err_str)
            return None
        date_obj.month = date_parts[1]
    if len(date_parts) > 2:
        if not len(date_parts[2]) == 2:
            print(err_str)
            return None
        date_obj.day = date_parts[2]
    return date_obj