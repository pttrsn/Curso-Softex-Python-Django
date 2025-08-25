
print('1. Avançar \n2. Recuar \n3. Status \n4. Reiniciar \n5. Desligar')

posicao = 0

while True:
    comando = int(input('Digite o comando desejado: '))
    if comando == 1:
        avancar = int(input('Digite a quantidade de posições para avançar: '))
        posicao += avancar
        print(f'O Robô avançou {avancar} posições...'.center(40))
    elif comando == 2:
        recuar = int(input('Digite a quantidade de posições para recuar: '))
        posicao -= recuar
        print(f'O Robô recuou {recuar} posições...'.center(40))
    elif comando == 3:
        print(f'A posição atual do Robô é {posicao}.'.center(40))

    elif comando == 4:
        print('Reiniciando o Robô...'.center(40))
        posicao = 0
    elif comando == 5:
        print('Desligando o Robô...'.center(40))
        break
    else:
        print('Comando inválido, tente novamente.'.center(40))