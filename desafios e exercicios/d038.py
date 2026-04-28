n1 = float(input('1 numero: '))
n2 = float(input('2 numero: '))
if n1 > n2:
    print('O maior valor e {:.1f}'.format(n1))
elif n2 == n1:
    print('Os valores são iguais')
else:
    print('O maior valor e {:.1f}'.format(n2))