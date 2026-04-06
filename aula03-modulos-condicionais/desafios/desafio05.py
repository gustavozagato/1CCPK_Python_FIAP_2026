num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 % num2 == 0 or num2 % num1 == 0:
    print('Eles são múltiplos')
else:
    print('Eles não são múltiplos')