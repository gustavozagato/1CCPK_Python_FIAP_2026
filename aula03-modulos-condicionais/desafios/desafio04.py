notas = input('Digite as notas: ').split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])
nota4 = float(notas[3])

media_final = (nota1+nota2+nota3+nota4) /4
resultado = ''
if media_final >= 7:
    resultado = 'Aprovado'
elif media_final >= 5 and media_final < 7:
    resultado = 'Em recuperação'
elif media_final < 5:
    resultado = 'Reprovado'

print(f'A média final é {media_final:.1f}')
print(resultado)
