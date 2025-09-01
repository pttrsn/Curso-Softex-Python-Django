lista1 = [ 'pêra', 'uva', 'laranja', 'tangerina' ]
lista2 = [ 'laranja', 'maça', 'tangerina', 'morango' ]
lista3 = [ 'banana' ]

frutas = [ item for item in lista1 if item in lista2 ]

if True:
    lista3.extend(frutas)
    print(lista3)

 