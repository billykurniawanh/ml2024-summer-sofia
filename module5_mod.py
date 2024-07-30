class NumberList:
    def __init__(self):
        self.numbers = []
        self.length = 0

    def set_length(self, number):
        self.length = number

    def insert(self, number):
        self.numbers.append(number)

    def search(self, number):
        if number in self.numbers:
            return self.numbers.index(number) + 1
        else:
            return -1