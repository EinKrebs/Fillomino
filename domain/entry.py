class Entry:
    @staticmethod
    def empty_entry():
        return Entry('.')

    def __init__(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("Invalid entry: numbers can be "
                                 "positive only")
            self.value = value
            self.empty = False
        elif isinstance(value, str):
            if value != '.':
                raise ValueError("Invalid entry")
            self.value = 0
            self.empty = True
        else:
            raise ValueError("Invalid entry type: only numbers and"
                             " '.' are allowed")
