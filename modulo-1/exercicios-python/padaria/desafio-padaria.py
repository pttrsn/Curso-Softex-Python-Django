paes = {
    '1.' : 'Pão Francês',
    '2.' : 'Pão de Forma',
    '3.' : 'Pão Doce',
}

pagamento = {
    '1' : 'Dinheiro',
    '2' : 'Cartão'
}

pedido = 0

print('PADARIA'.center(100))

print('Olá! Bem-vindo(a).')
for num, pao in paes.items():
    print(num, pao)
input('Escolha o número do pão: ')
if paes.key(1):
    print('Pão Francês.')




