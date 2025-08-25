def mostrar_trajetoria(posicao):
    verde = '\033[92m'
    vermelho = '\033[91m'
    amarelo = '\033[93m'
    reset = '\033[0m'
    if posicao > 0:
        print("Trajetória: " + f"{verde}{'>>' * posicao}{reset} {amarelo}R{reset}")
    elif posicao < 0:
        print("Trajetória: " + f"{vermelho}{'<<' * abs(posicao)}{reset} {amarelo}R{reset}")
    else:
        print(f"Trajetória: {amarelo}R (início){reset}")

print('1. Avançar \n2. Recuar \n3. Status \n4. Reiniciar \n5. Desligar')

posicao = 0

while True:
    comando = int(input('Digite o comando desejado: '))
    if comando == 1:
        avancar = int(input('Digite a quantidade de posições para avançar: '))
        posicao += avancar
        print(f'O Robô avançou {avancar} posições...'.center(40))
        mostrar_trajetoria(posicao)
    elif comando == 2:
        recuar = int(input('Digite a quantidade de posições para recuar: '))
        posicao -= recuar
        print(f'O Robô recuou {recuar} posições...'.center(40))
        mostrar_trajetoria(posicao)
    elif comando == 3:
        print(f'A posição atual do Robô é {posicao}.'.center(40))
        mostrar_trajetoria(posicao)
    elif comando == 4:
        print('Reiniciando o Robô...'.center(40))
        posicao = 0
        mostrar_trajetoria(posicao)
    elif comando == 5:
        print('Desligando o Robô...'.center(40))
        break
    else:
        print('Comando inválido, tente novamente.'.center(40))