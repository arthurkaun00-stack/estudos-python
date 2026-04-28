num = int(input('Digite um numero inteiro: '))
print('''Escolha uma opção: 
[1]Binario
[2]Octal
[3]Hexadecimal ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O valo {} em binario e {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O valo {} em octal e {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('O valo {} em hexadecimal e {}'.format(num,hex(num)[2:]))
else:
    print('Opção Invalida!')