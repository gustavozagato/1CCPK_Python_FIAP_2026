def eh_primo(n):
    div = 0
    for i in range(1,n,1):
        if i != 1 and i != n:
            if n % i != 0:
                div += 1

    if div == n-2:
        primo = True
    else:
        primo = False
    return primo

contador = 0

for i in range(2000):
    if eh_primo(i):
        contador +=1

print(contador)