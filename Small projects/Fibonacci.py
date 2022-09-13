def Fibonacci(n):
    for i in range(n): print(int((1/(5**(1/2)))*(((1+5**(1/2))/2)**i-((1-5**(1/2))/2)**i)),end=' ')
n = int(input('Amount of elements: '))
Fibonacci(n)
def Fibonnaci_Element(m):
    return print('Element', m, 'of the Fibonacci sequence is', int((1/(5**(1/2)))*(((1+5**(1/2))/2)**(m-1)-((1-5**(1/2))/2)**(m-1))))
m = int(input('\nGive the nth element: '))
Fibonnaci_Element(m)



