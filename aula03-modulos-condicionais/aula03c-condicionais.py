# ESTRUTUTA CONDICIONAL SIMPLES

nota = 5.0

if nota < 6:
    print(f'Sua nota é {nota}')

# ESTRUTURA CONDICIONAL COMPOSTA

nota_final = 5.0

if nota_final < 6:
    print('Reprovado')
else:
    print('Aprovado')

# ESTRUTURA CONDICIONAL ENCADEADA

nota_final = 7.0

if nota_final < 4:
    print('Reprovado')
else:
    if nota_final < 6:
        print('Recuperação')
    else:
        print("Aprovado")

# ESTRUTURA CONDIOCIONAL ENCADEADA - ELIF

nota_final = 2.0

if nota_final < 4:
    print('Reprovado')
elif nota_final < 6:
    print('Recuperação')
else:
    print("Aprovado")
