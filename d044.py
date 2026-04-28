print('''


''')
prod = float(input("Preço do produto: "))
print('''==============================
Escolha a forma de pagamento!
[1]Dinheiro/cheque
[2]Cartão
[3]2x no cartão
[4]3x ou mais no cartão
==============================''')
opcao = int(input('Escolha uma opção: '))

if  opcao == 1:
    print('Você teve um desconto de 10% preço a pagar R${:.2f} parabens🎉!!!'.format(prod*0.90))
elif opcao == 2:
    print('Você teve um desconto de 5% preço a pagar R${:.2f} parabens🎉!!!'.format(prod*0.95))
elif opcao == 3:
    print('Você pagara 2x R${:.2f} preço total a pagar R${:.2f} '.format(prod/2,prod))
elif opcao == 4:
    tot = prod *1.20
    parc = int(input('Qual será a quantidade de parcelas?: '))
    print('Você pagara {:.0f} de R${:.2f} preço total a pagar R${:.2f} contém 20% de juros'.format(parc,tot/parc,tot))
else:
    print('\033[31;40m Opçao Invalida!!! \033[m')