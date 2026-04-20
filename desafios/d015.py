km = float(input('Quantos km foi rodado: '))
dia = float(input('Quantos dias foi usada: '))
pk =km*0.15
pd =dia*60
tot = pd+pk
print('Valores a pagar, km :{:.2f} dias de uso:{:.2f} \ntotal a pagar {:.2f}'.format(pk,pd,tot))