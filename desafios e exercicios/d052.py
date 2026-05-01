num = int(input('Digite um numero?: '))
cont = 0
for c in range(1,num+1):
    if num%c == 0:
        print(f'\033[31;40m {c} \033[m', end='')
        cont += 1
    else:
        print(f'\033[33;40m {c} \033[m', end='')
if cont == 2:
    res = 'Sim'
else:
    res = 'Não'
print()
print(f'Quantidade de numeros diviveis: {cont}')
print(f'O nùmero é primo? {res}')
