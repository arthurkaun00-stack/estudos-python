a = int(input('1 lado: '))
b = int(input('2 lado: '))
c = int(input('3 lado: '))

if c < a+b and b < a+c and a < b+c:
    print('E uma triangulo')
    if a == b == c:
        print('E uma triangulo Equilatero')
   
    elif a != b != c != a:
        print('E uma triangulo Escaleno')
    else:
        print('E uma triangulo Isósceles')
else:
    print('\033[1;31;40m Não E uma triangulo \033[m')


