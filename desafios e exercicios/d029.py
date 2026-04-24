km = int(input('Velocidade do carro: '))
if km > 80:
    print('Voce foi multado \nMulta foi de R${:.2f}'.format((km-80)*7))
else:
    print('Velocidade correta 👍 ')