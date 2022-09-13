import math as m

from matplotlib import pyplot as p


def ln(x):
    return m.log(x,m.exp(1))

b = int(input('Dosis: '))
t = int(input('Halfwaarde tijd: '))
d = int(input('Aantal dagen: '))
k = -ln((1/2))/t
arr = []
y = 0
def dosis(x):
    y = 0
    for i in range(0, d+1): y += b*m.exp(-k*(x-24*i))
    return y
for x in range(0,24*(d+1)+1):
    arr.append(dosis(x))
x = list(range(0,24*(d+1)+1))
if d>1: print('Na', d, 'dagen is er nog', round(dosis(d*24),2), 'mg aanwezig is het lichaam')
else: print('Na', d, 'dag is er nog', round(dosis(d*24),2), 'mg aanwezig is het lichaam')
p.xlim(24*d, 24*(d+1))
p.ylim(0, 100)
p.plot(x,arr)
p.xlabel('Tijd')
p.ylabel('Aantal mg')
p.title('Grootte van de dosis aanwezig in het lichaam')
p.show()
