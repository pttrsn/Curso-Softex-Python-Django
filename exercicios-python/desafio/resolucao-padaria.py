#Nome dos pães
nome_frances = 'Francês'
nome_doce = 'Doce'
nome_forma = 'Forma'

#Valor dos pães
valor_frances = 0.50
valor_doce = 6.00
valor_forma = 5.99

#Quantidade dos pães
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 10

#Nome do atendente
nome_atendente = 'Maria'

#Bairros atendidos para entrega
bairro_barroco = 'barroco'
bairro_sao_jose = 'sao jose'

#Frete
frete_barroco = 5.00
frete_sao_jose = 15.00

#Código de venda
codigo_venda = 8532

while True:
    print(f'-- Bem vindo à Padaria Desespero, sou a atendente {nome_atendente}.')
    escolha = input(f'Temos os pães: {nome_frances}, {nome_doce}, {nome_forma}. Qual pão você deseja?')

    #Pedido do Pão Francês
    if escolha == nome_frances:
        quantidade = int(input('Qual a quantidade? '))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f'Seu pedido ficou em R${valor_compra}.')
        else:
            print(f'Infelizmente só temos {quantidade_frances} no momento.')
            break

    #Cálculo de entrega
    forma_retirada = input('É para 1: retirar ou 2: entregar? ').lower()
    if forma_retirada == '2':
        bairro_entrega = input(f'Qual o bairro? (1:{bairro_barroco} ou 2:{bairro_sao_jose}).')
        if bairro_entrega == '1':
            valor_frete = frete_barroco
            print(f'Valor do frete R${valor_frete}.')
        elif bairro_entrega == '2':
            valor_frete = frete_sao_jose
            print(f'Valor do frete R${valor_frete}.')
        else:
            print('Fora da área de entrega.')
            break
    elif forma_retirada == '1':
        valor_frete = 0.00
    else:
        break