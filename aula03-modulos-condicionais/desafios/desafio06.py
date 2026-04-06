def calculadora(num1,num2,operacao):
    resultado = 0
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    return resultado

num1 = int(input('Digite um número: '))
operacao = input('Digite a operação: ')
num2 = int(input('Digite outro número: '))

print(f'O resultado é {calculadora(num1,num2,operacao)}')