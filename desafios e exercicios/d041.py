from datetime import date
atual = date.today().year
nasc = int(input('Que ano voce nasceu?: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
print('Classificação: ',end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')