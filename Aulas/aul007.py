n1 = int(input('Digite um numero: '))
n2 = int(input('Outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('soma {} \n multiplicação {} \n divisao {:.3} '.format(s,m,d), end=' ')
print('divisao inteira {} \n expotencialização {} '.format(di,e))