temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
salas = [1, 2, 3, 4]
media = []
criticos = []
soma_temp = 0
soma_criticos = 0
temp_critico = 0
n = 0

for sala in temperaturas:
    for temperatura in sala:
        soma_temp += temperatura
        if temperatura >= 33:
            soma_criticos += 1
    criticos.append(soma_criticos)
    soma_criticos = 0
    soma_temp = soma_temp / len(sala)
    media.append(soma_temp)
    soma_temp = 0

for i in range(len(criticos)):
    if criticos[i] > temp_critico:
        temp_critico = criticos[i]
        n += 1

for i in range(len(salas)):
    print(f'Sala {salas[i]}')
    print(f'Média: {media[i]}')
    print(f'Registros críticos: {criticos[i]}')
    print('')

print(f'Sala com maior risco: Sala {salas[n]}')