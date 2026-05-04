nomes = ['Max', 'Bob', 'Carlos', 'Ana']

for i in range(len(nomes)):
    for j in range(len(nomes)):
        if i != j:
            if i < j:
                print(f'{nomes[i]} - {nomes[j]}')

print()

for i in range(len(nomes)):
    for j in range(i+1,len(nomes)):
        print(f'{nomes[i]} - {nomes[j]}')
