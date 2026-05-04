import random

sala = []
n = int(input('Digite um número: '))
notas = 0
maior = 0
menor = 0
igual = 0

for i in range(n):
    sala.append(random.uniform(0,10))
    notas += sala[i]

media = notas / len(sala)

for nota in sala:
    if nota > media:
        maior += 1
    elif nota < media:
        menor += 1
    else:
        igual += 1

print(sala)
print(f'iguais: {igual}')
print(f'maior: {maior}')
print(f'menor: {menor}')
