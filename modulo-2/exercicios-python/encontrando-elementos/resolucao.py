lista1 = [ 'pêra', 'uva', 'laranja', 'tangerina' ]
lista2 = [ 'laranja', 'maça', 'tangerina', 'morango' ]
comum = []

for fruta in lista1:
    if fruta in lista2 and fruta not in comum:
        comum.append(fruta)

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Frutas em comum: {comum}')
 