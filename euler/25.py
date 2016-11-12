
class Fibonacci():
    def __init__(self, no_of_digits):
        self.no_of_digits = no_of_digits

    def find_term(self):

        i = 3
        fib_n_2 = 1
        fib_n_1 = 1
        while True:
            fib_n = fib_n_1 + fib_n_2
            if len(str(fib_n)) == self.no_of_digits:
                return i
            fib_n_2 = fib_n_1
            fib_n_1 = fib_n
            i += 1

fib = Fibonacci(1000)
term = fib.find_term()
print term
