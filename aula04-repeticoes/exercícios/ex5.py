maior = 0
for i in range(5):
    n = int(input('Digite um número: '))
    if maior < n:
        maior = n
print(maior)