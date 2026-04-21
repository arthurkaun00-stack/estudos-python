n = int(input('Digite um numero '))
print('numero digitado {} \nunidade {} \ndezena  {} \ncentena {} \nmilhar  {} '.format(n,n//1 %10,n//10 %10,n//100 %10,n//1000 %10))