a = int(input('Valor 1:'))
b = int(input('Valor 2:'))
c = int(input('Valor 3:'))
if c < a+b and b < a+c and a < b+c:
    print('E uma triangulo')
else:
    print('\033[1;31;40m Não E uma triangulo \033[m')