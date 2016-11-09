def get_diagnol_sum(n):
    i = 3
    sum = 1
    while i <= n:
        sum = sum + (i**2 + (i**2 - i + 1) + (i**2 -2*i + 2) + (i**2 - 3*i + 3))
        i += 2

    return sum

s = get_diagnol_sum(1001)
print s
