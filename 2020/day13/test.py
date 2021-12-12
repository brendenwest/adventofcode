from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__ == '__main__':
#    n = [3, 5, 7]
    n = [7,13,59,31,19]
#    n = [17, 13, 19]
#    a = [2, 3, 2]
    a = [4, 3, 0, 29, 16]
#    a = [3, 1, 0]
#{31: 6, 19: 7, 59: 4, 13: 1, 7: 0}

#    print(chinese_remainder(n, a))