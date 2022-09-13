"""
The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. 
If you repeat the process continuously for n, n will eventually reach 1.

Write a program that will output the length of the Collatz Conjecture for any given n.
"""

n = int(input('Starting number: '))

def collatz(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
            counter += 1
        else:
            n = n * 3 + 1
            counter += 1
    return print(counter)

collatz(n)