km = float(input('Distancia percorrida: '))
if km <= 200:
    print('Valor da corrida R$ {}'.format(km*0.5))
else:
    print('Valor da corrida R$ {}'.format(km*0.45))