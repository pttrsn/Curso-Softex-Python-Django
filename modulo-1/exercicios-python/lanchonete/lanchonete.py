print('Lanchonete'.center(50,'='))

nome_hamburguer = 'Hambúrguer'
valor_hamburguer = 20.99

cupom = 15

while True:
    pedido = str(input(f'Catálogo: \n- {nome_hamburguer} \nFaça seu pedido: '))
    if pedido == nome_hamburguer:
        desconto = int(input('Cupom de desconto disponível. Deseja utilizar? \n1. Sim \n2. Não \n: '))
        if desconto == 1:
            preco = valor_hamburguer - (valor_hamburguer * cupom / 100)
            print(f'O valor total do pedido foi de R${preco:.2f}. \nAgradecemos a preferência!')
            break
        elif desconto == 2:
            print(f'O valor total do pedido foi de R${valor_hamburguer:.2f}. \nAgradecemos a preferência!')
            break
        else:
            print('Sentimos muito! Ocorreu um erro durante o pedido, tente novamente.')