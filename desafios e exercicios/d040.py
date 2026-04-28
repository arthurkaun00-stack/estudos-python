n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2
if media > 6:
    print('APROVADO a media {}'.format(media))
elif media < 4:
    print('REPROVADO a media {}'.format(media))
else:
    print('RECUPERÇÃO a media {}'.format(media))