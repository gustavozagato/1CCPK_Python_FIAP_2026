ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = 2026 - ano_nasc

if idade >= 16 and idade < 18 or idade > 70:
    print('Voto opcional')
elif idade < 16:
    print('Voto proibido')
else:
    print('Voto obrigatório')
