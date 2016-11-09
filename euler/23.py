#  This is a solution to Euler project problem No: 23

import math


def is_abundant_number(num):
    factors = get_factors(num)
    total_of_factors = sum(factors)
    if total_of_factors > num:
        return True
    return False


def get_factors(num):
    i = 1
    factors = []
    while i < math.ceil(math.sqrt(num)):
        if num % i == 0:
            factors.append(i)
            if num/i != i:
                factors.append(num/i)
        i += 1

    if i*i == num:
        factors.append(i)

    factors.remove(num)
    return factors


def get_combinations(abundant_numbers, lim):

    i = 0
    all_dict = {}
    max_num = len(abundant_numbers)
    while i < max_num:
        a = abundant_numbers[i]
        j = i

        if 2*a > lim:
            break

        while j < max_num:
            b = abundant_numbers[j]
            c = a + b
            if c > lim:
                break
            all_dict[c] = 1
            j += 1
        i += 1

    total = 0
    i = 1
    while i < lim:
        if i not in all_dict:
            total += i

        i += 1

    print total


def main():
    i = 2
    lim = 28123
    abundant_numbers = []
    while i < lim:
        if is_abundant_number(i):
            abundant_numbers.append(i)
        i += 1

    get_combinations(abundant_numbers, lim)


if __name__ == "__main__":
    main()
