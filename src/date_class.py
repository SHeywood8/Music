class Date():
    def __init__(self, year:int, month:int = None, day:int = None):
        self.year = int(year)
        if month != None:
            self.month = int(month)
        else:
            self.month = month
        if day != None:
            self.day = int(day)
        else:
            self.day = day

    def __repr__(self):
        string = str(self.year)
        if self.month != None:
            string += '-' + str(self.month)
        else:
            string += '-mm'
        if self.day != None:
            string += '-' + str(self.day)
        return string

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        # Only equal if all 3 fields are equal
        return (self.year == other.year and self.month == other.month and self.day == other.day)

    def __ne__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        # Not equal if any field differs
        return (self.year != other.year or self.month != other.month or self.day != other.day)

    def __gt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented

        # Compare years
        if self.year < other.year:
            return False
        elif self.year > other.year:
            return True
        # Only compares months if years are equal
        try:
            if self.month < other.month:
                return False
            elif self.month > other.month:
                return True
        except:
            if self.month != other.month:
                return False
        # Only compares days if years and months are equal
        try:
            if self.day <= other.day:
                return False
            else:
                return True
        except:
            return False

    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented

        # Compare years
        if self.year > other.year:
            return False
        elif self.year < other.year:
            return True
        # Only compares months if years are equal
        try:
            if self.month > other.month:
                return False
            elif self.month < other.month:
                return True
        except:
            if self.month != other.month:
                return False
        # Only compares days if years and months are equal
        try:
            if self.day >= other.day:
                return False
            else:
                return True
        except:
            return False

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def get_format(self):
        format = 'yyyy'
        if self.month != None:
            format += '-mm'
        if self.day != None:
            format += '-dd'
        return format


def str_to_date(date_str:str):
    err_str = "Invalid date format, please use 'yyyy-mm-dd'."
    if date_str == '':
        print(err_str)
        return None
    date_parts = date_str.split("-")

    # Add year (required)
    year = date_parts[0]
    if not len(year) == 4:
        print(err_str)
        return None
    try:
        year = int(year)
    except:
        print("Year must be a four digit integer.")
        return None
    date_obj = Date(year)

    # Add month
    if len(date_parts) > 1:
        month = date_parts[1]
        if not len(month) == 2:
            print(err_str)
            return None
        try:
            month = int(month)
        except:
            print("Month must be a two digit integer.")
            return None
        if month > 12 or month < 1:
            print("Month must be an integer between 1 and 12.")
            return None
        date_obj.month = month

    # Add day
    if len(date_parts) > 2:
        day = date_parts[2]
        if not len(day) == 2:
            print(err_str)
            return None
        try:
            day = int(day)
        except:
            print("Day must be a two digit integer.")
            return None
        if day > 31 or day < 1:
            print("Month must be an integer between 1 and 31.")
            return None
        date_obj.day = day
    return date_obj

if __name__ == "__main__":
    print(Date(2026,day = 1) != Date(2026,day = 2))
