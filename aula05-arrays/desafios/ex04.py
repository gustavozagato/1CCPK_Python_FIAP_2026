import random

vetor = []
n = int(input('Digite um número: '))
soma = 0

for i in range(n):
    vetor.append(random.randint(1,100))
    soma += vetor[i]

print(vetor)
print(soma)
