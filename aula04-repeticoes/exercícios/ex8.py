n = int(input('Digite um número: '))

while n < 0:
    print('Digite apenas números inteiros!')
    n = int(input('Digite um número: '))

for i in range(1,n,1):
    if n % i == 0:
        print(i)