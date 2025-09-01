
print('1. Avançar \n2. Recuar \n3. Status \n4. Desligar')

posicao = 0

while True:
    comando = int(input('Digite o comando desejado: '))
    if comando == 1:
        posicao += 1
        print('O Robô avançou uma posição...'.center(40))
    elif comando == 2:
        posicao -= 1
        print('O Robô recuou uma posição...'.center(40))
    elif comando == 3:
        print(f'A posição atual do robô é {posicao}.'.center(40))
    elif comando == 4:
        print('Desligando o robô...'.center(40))
        break
    else:
        print('Comando inválido, tente novamente.'.center(40))