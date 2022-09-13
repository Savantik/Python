"""
We want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k*n.
eg. digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""
n = int(input('Number: '))
p = int(input('Raise to the power of: '))
def dig_pow(n, p):
    n = str(n)
    LHS = 0
    for digit in n:
        LHS += int(digit)**p
        p += 1
    k = LHS/int(n)
    if k == int(k): return print(int(k))
    else: return print(-1)

dig_pow(n,p)