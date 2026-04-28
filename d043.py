peso = float(input('Qual e seu peso?: '))
altura = float(input('Qual e seu altura?: '))
imc = peso / (altura ** 2)
print('seu imc é {:.1f} !'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('peso ideal')
elif imc > 25 and imc < 30:
    print('sobre peso')
elif imc > 30 and imc < 40:
    print('obsidade')
elif imc > 40:
    print('obsidade mórbia')