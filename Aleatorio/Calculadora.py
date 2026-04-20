from math import sqrt
import pygame
print('===============')
print('  CALCULADORA  ')
print('===============')
n1 = float(input('Escreva um numero: '))
n2 = float(input('Escreva outro numero: '))
print('+ - x / x2 V')
operacao = input('Escreva tipo de operação ')

if operacao == '+':
    res = n1 + n2
elif operacao == '-':
    res = n1 + n2
elif operacao == 'x':
    res = n1 * n2
elif operacao == '/':
    res = n1 / n2
elif operacao == 'x2':
    res = n1 **n2
elif operacao == 'V':
    raiz1 = sqrt(n1) 
    raiz2 = sqrt(n2)
    res = f"Valor 1: {raiz1:.2f} | Valor 2: {raiz2:.2f}"
else:
    res = 'Operação Invalida‼️ ❌'
pygame.init()
pygame.mixer.music.load('Aleatorio/Sininho.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pass
print('Resultado: {} 😁'.format(res))