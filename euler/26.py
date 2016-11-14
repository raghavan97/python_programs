
class ReciprocalCycles():
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.max_recur_len = 0
        self.divisor = 0

    def reciprocal(self, divisor):
        num = 1

        places = 1
        div_dict = {}
        recur_len = 0
        while True:
            dividend = num / divisor
            if dividend == 0:
                num = num * 10
                continue
            remainder = num % divisor
            if remainder == 0:
                recur_len = 0
                break
            if (num, divisor) in div_dict:
                old_place = div_dict[(num, divisor)]
                recur_len = places - old_place
                break

            div_dict[(num, divisor)] = places
            num = remainder
            places += 1

        if recur_len > self.max_recur_len:
            self.max_recur_len = recur_len
            self.divisor = divisor

    def find_longest_recur_cycle(self):
        i = 2
        while i < self.max_limit:
            self.reciprocal(i)
            i += 1

    def print_max(self):
        print 'max recur len={} divisor={}'.format(
            self.max_recur_len, self.divisor
        )

rc = ReciprocalCycles(1000)
rc.find_longest_recur_cycle()
rc.print_max()
