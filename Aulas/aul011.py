#a = 6
#b = 100
#print('\033[m Os valores sao \033[1;30;47m{}\033[m e \033[4;37;41m{}\033[m'.format(a,b))
nome = 'Arthur'
cores = {'limpar':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'pretobranco':'\033[1;30;47m'}
print('Seu nome é {}{}{}? '.format(cores['vermelho'],nome,cores['limpar']))