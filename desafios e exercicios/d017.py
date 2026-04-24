'''maneira tradicional
n1 = float(input('comprimento do cateto oposto: '))
n2 = float(input('comprimento do cateto adiacente: '))
res = (n1**2+n2**2)**(1/2)
print('valor do oposto {} valor do adiacente {} valor da hipotenusa {}'.format(n1,n2,res))'''

import math
n1 = float(input('comprimento do cateto oposto: '))
n2 = float(input('comprimento do cateto adiacente: '))
res = math.hypot(n1,n2)
print('Valor da hipotenusa {:.2f}'.format(res))