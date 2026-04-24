sal  = float(input('Seu salario: '))
if sal > 1250:
    print('Aumento de salario foi de 10% \nSalario altual R${:.2f}'.format((sal*1.10)))
else:
    print('Aumento de salario foi de 15% \nSalario altual R${:.2f}'.format((sal*1.15)))