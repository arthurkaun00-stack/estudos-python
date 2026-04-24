import random
v = random.randint(1,5)
c = int(input('numero de 1 a 5: '))
print('Acertou é'if c == v else 'errou o numero e',v)