import math
import copy


class LexicOrder():
    def __init__(self, posn, digits):
        self.posn = posn
        self.all_digits = digits

    def find_number(self):
        width = len(self.all_digits)
        i = width
        combinations = {}
        while i >= 1:
            combinations[i] = math.factorial(i-1)
            i -= 1

        available_digits = copy.deepcopy(self.all_digits)

        number = []
        place = width
        posn = self.posn -1  # posn starts from 0
        while place >= 1:
            temp = posn/combinations[place]
            digit = available_digits[temp]
            number.append(digit)
            del available_digits[temp]
            posn = posn % combinations[place]
            place -= 1

        number_str = ''.join([str(i) for i in number])
        return number_str

if __name__ == '__main__':
    lo = LexicOrder(10**6, range(10))
    number = lo.find_number()
    print number
