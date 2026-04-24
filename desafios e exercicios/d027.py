n = input('nome: ').strip()
print('Seja bem vindo',n)
nome= n.split()
print('Primeiro nome: {} \nultimo nome: {}'.format(nome[0],nome[len(nome)-1]))