def Fibonacci(n):
    for i in range(n): print(int((1/(5**(1/2)))*(((1+5**(1/2))/2)**i-((1-5**(1/2))/2)**i)),end=' ')
n = int(input('Geef het aantal elementen: '))
Fibonacci(n)
def Fibonnaci_Element(m):
    return print('Element', m, 'van de rij van Fibonacci is', int((1/(5**(1/2)))*(((1+5**(1/2))/2)**(m-1)-((1-5**(1/2))/2)**(m-1))))
m = int(input('\nGeef het hoeveelste element: '))
Fibonnaci_Element(10)



