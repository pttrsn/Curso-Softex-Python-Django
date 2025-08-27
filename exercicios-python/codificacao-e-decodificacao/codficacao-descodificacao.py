count = 0

while count < 5:
    pal = input('Escreva uma palavra: ')
    cod = pal
    cod = cod.replace('a','1')
    cod = cod.replace('e','2')
    cod = cod.replace('i','3')
    cod = cod.replace('o','4')
    cod = cod.replace('u','5')

    dec = cod
    dec = dec.replace('1','a')
    dec = dec.replace('2','e')
    dec = dec.replace('3','i')
    dec = dec.replace('4','o')
    dec = dec.replace('5','u')
    
    count += 1

    print(f'{cod}')
    print(f'{dec}')