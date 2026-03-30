idade = int(input('Digite sua idade: '))

if idade >= 16 and idade < 18 or idade > 70:
    print('Voto opcional')
elif idade < 16:
    print('Não vota')
else:
    print('Voto obrigatório')
