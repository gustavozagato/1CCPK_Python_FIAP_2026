n = int(input('Digite um número: '))

while n < 0:
    print('Digite apenas números inteiros!')
    n = int(input('Digite um número: '))

soma = n
for i in range(n):
    soma+=i

print(f'a soma final de 1 até {n} é de {soma}')