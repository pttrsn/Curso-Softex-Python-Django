while True:
    telefone = input('Digite um número de telefone: ')

    repeticao = any(telefone.count(digito) > 2 for digito in set(telefone))

    if telefone.isdigit() and len(telefone) == 11 and repeticao == False:
        print(f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:11]}')
        break
    elif not telefone.isdigit():
        print('O telefone não pode conter letras ou caracteres especiais.')
    elif len(telefone) < 11:
        print('O telefone não pode conter menos de 11 números.')
    elif len(telefone) > 11:
        print('O telefone não pode conter mais de 11 números.')
    elif repeticao:
        print('O telefone não pode conter mais de 3 números repetidos.')
    else:
        pass