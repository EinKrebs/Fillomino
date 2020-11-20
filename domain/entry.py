class Entry:
    @staticmethod
    def get_empty():
        return Entry('.')

    def __init__(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("Invalid entry: numbers can be "
                                 "positive only")
            self.value = value
            self.empty = False
        elif isinstance(value, str):
            try:
                self.value = int(value)
                self.empty = False
            except ValueError:
                if value != '.':
                    raise ValueError("Invalid entry")
                self.value = 0
                self.empty = True
        else:
            raise TypeError("Invalid entry type: only numbers and"
                            " '.' are allowed")

    def __eq__(self, other):
        if isinstance(other, Entry):
            if other.empty:
                return self.empty
            else:
                return not self.empty and self.value == other.value
        elif isinstance(other, int):
            return not self.empty and self.value == other
        return False

    def __str__(self):
        return '.' if self.empty else str(self.value)
