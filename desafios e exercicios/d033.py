a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
menor = a
maior = a
'''Menor'''
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
'''Maior'''
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('Menor numero {} Menor numero {}'.format(menor,maior))