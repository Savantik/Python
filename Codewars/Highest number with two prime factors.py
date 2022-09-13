#Highest possible value bounded by n of two primes p1 and p2 multiplied
p1 = int(input('First prime number: '))
p2 = int(input('Second prime number: '))
n = int(input('Boundary: '))

def highest_biPrimefac(p1, p2, n): # p1, p2 primes and p1 < p2
        while True:
            i = 1
            j = 1
            while n%(p1**i) == 0: i += 1
            while n%(p2**j) == 0: j += 1
            i -= 1
            j -= 1
            if n/(p1**i*p2**j) == 1 and i>0 and j>0: return print([p1**i*p2**j,i,j]) #highest value, power of p1, power of p2
            else: n -= 1
highest_biPrimefac(p1,p2,n)