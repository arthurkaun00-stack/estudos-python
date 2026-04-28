casa = float(input('Qual e o valor: R$'))
sala = float(input('Qual e seu salario: R$'))
anos = float(input('Quantos anos vai paga: '))
prestaçao = casa/(anos*12)
minimo = prestaçao * 30/1000
print('Para pagar uma casa de R${:.2f} em {} ano'.format(casa,anos), end='')
print(' prestaçao sera de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('empretimo pode ser concedido')
else:
    print('empretimo nao pode ser concedido')