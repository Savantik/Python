#Adaptating Legendre's formula to find the trailing zeros of n factorial
n = int(input('Give factorial: '))
def zeros(n):
    counter = 0
    while n >= 5:
        n //= 5
        counter += n
    return print(counter)

zeros(n)



    