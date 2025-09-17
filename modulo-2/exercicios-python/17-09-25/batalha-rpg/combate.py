import time


def batalha(heroi, monstro):
    while heroi.estar_vivo() and monstro.estar_vivo():
        print(f'\nVida do Herói: {heroi.vida} |'
               f'Vida do Monstro: {monstro.vida}')
            
        print('\nEscolha sua ação:')
        print('1) Atacar')
        print('2) Defender')
        print('3) Usar Poção')
        print('4) Fugir')
        escolha = input('Digite o número da ação: ')

        if escolha == '1':
                heroi.atacar(monstro)
        elif escolha == '2':
            heroi.defender()
            print(f'{heroi.nome} vai defender o próximo ataque!')
        elif escolha == '3':
            heroi.usar_pocao()
        elif escolha == '4':
            print(f'{heroi.nome} fugiu da batalha!')
            break
        else:
            print('Escolha inválida! O turno foi perdido.')
            
        if not monstro.estar_vivo():
            print('O Herói venceu!')
            break

        time.sleep(1)
        monstro.atacar(heroi)

        if not heroi.estar_vivo():
            print('O monstro venceu!')
            break

        time.sleep(1)