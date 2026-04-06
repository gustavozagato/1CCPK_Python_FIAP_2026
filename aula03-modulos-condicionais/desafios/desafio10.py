def triangulo(A,B,C):
    resultado = ''
    if  A == B == C:
        resultado = 'Triângulo equilatero'
    elif B == C:
        resultado = 'Triângulo isósceles'
    elif A**2 == B**2 + C**2:
        resultado = 'Triângulo retângulo'
    elif A**2 > B**2 + C**2:
        resultado = 'Triângulo obtusângulo'
    elif A**2 < B**2 + C**2:
        resultado = 'Triângulo acutângulo'
    elif A >= B+C:
        resultado = 'Não forma triângulo'
    return resultado

lados = []
valor1 = int(input('Digie o primeiro lado: '))
valor2 = int(input('Digie o segundo lado: '))
valor3 = int(input('Digie o terceiro lado: '))
lados.append(valor1)
lados.append(valor2)
lados.append(valor3)
lados.sort(reverse=True)
A = lados[0]
B = lados[1]
C = lados[2]

print(f'O resultado é: {triangulo(A,B,C)}')