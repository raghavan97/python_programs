import math
import sys

class TruncatablePrimes():
    def __init__(self):
        self.primes={}

    def gen_trunc_nums(self, num):
        posn=1
        n = len(num)
        trunc_list = []
        while posn < n:
            trunc_list.append(num[:posn])
            trunc_list.append(num[posn:])
            posn += 1

        trunc_list.append(num)

        trunc_dict = {}
        for i in trunc_list:
            ind = len(i)
            if ind not in trunc_dict:
                trunc_dict[ind] = []
            trunc_dict[ind].append(i)

        ordered_list = []
        ls = trunc_dict.keys()
        ls.sort()
        for k in ls:
            temp = trunc_dict[k]
            temp.sort()
            ordered_list.extend(temp)

        return ordered_list

    def is_trunc_prime(self, num):
        trunc_list = self.gen_trunc_nums(num)
        for i in trunc_list:
            if not self.is_prime(int(i)):
                return False

        return True

    def get_all_truncated_primes(self):
        num = 9
        trunc_primes = []
        while True:
            if self.is_trunc_prime(str(num)):
                print num
                trunc_primes.append(num)
                if len(trunc_primes) >= 11:
                    print sum(trunc_primes)
                    return
            num += 2

    def is_prime(self,num):
        i = 2

        if num in (1,4,6,8,9):
            return False

        if num in (2,3,5,7):
            return True

        if num in self.primes:
            return self.primes[num]

        while i <= math.sqrt(num):
            if num%i == 0:
                self.primes[num] = False
                return False
            i +=1
        self.primes[num] = True
        return True

t = TruncatablePrimes()
t.get_all_truncated_primes()

