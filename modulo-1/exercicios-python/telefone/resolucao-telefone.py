numero = input('Digite O número de telefone: ')

if len(numero) != 11:
    print('Número com tamanho incorreto.')
elif not numero.isdigit():
    print('Não é possível gerar um número de telefone com esses valores.')
else:
    valido = True
    for c in numero:
        count = 0
        for d in numero:
            if d == c:
                count += 1
            if count >= 3:
                valido = False
                break

if not valido:
    print('Não é possível gerar um número de telefone com esses valores.')
else:
    print(
        '('
        + numero[0]
        + numero[1]
        + ') '
        + numero[2]
        + numero[3]
        + numero[4]
        + numero[5]
        + numero[6]
        + '-'
        + numero[7]
        + numero[8]
        + numero[9]
        + numero[10]
    )