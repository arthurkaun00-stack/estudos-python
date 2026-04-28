from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimeto: '))
idade = atual-nasc
print('Quem nasceu {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('Se aliste IMEDIANTAMENTE')
elif idade > 18:
    saldo = idade-18
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    print('Ano que voce deveria ter se alistado {}',format(atual-saldo))
else:
    saldo = 18-idade
    print('Você vai se alista daqui {} anos'.format(saldo))
    print('Ano que voce vai se alistar {}'.format(saldo+atual))