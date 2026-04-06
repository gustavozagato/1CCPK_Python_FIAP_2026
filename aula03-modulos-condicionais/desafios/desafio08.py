def aumento(salario):
    aumento = 0
    if salario <= 280:
        aumento = 20
    elif salario > 280 and salario < 700:
        aumento = 15
    elif salario >= 700 and salario < 1500:
        aumento = 10
    else:
        aumento = 5
    return aumento

salario = int(input('Digite o seu salário: '))
aumento = aumento(salario)
valor_aumento = salario * aumento/100
salario_final = salario + valor_aumento

print(f'Salário atual: {salario}')
print(f'Percentual de aumento: {aumento}')
print(f'Valor do aumento: {valor_aumento}')
print(f'Salário reajustado: {salario_final}')
