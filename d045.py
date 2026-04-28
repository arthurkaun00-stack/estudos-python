import random
print('''





''')
jogador = input('Jokenpô: ').lower() 
robo = random.choice(["pedra","papel","tesoura"])
print('O robo jogou {}'.format(robo))
if jogador == robo:
    res = "EMPATE"
elif (jogador == "pedra" and robo == "tesoura") or (jogador == "papel" and robo == "pedra") or (jogador == "tesoura" and robo == "papel"):
    res = "VENCEU"
else:
    res = "PERDEU"
print('Você {} !!!'.format(res))