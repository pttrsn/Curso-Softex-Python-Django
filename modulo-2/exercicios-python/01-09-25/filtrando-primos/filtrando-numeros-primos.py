lista1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
primos = []




for numero in lista1:
    primo = numero % 1 == 0 and numero % numero == 0
    if numero == primo:
        primos.append(primo)

print(primos) 