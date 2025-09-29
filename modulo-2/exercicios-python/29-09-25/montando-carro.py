class Motor:
    def ligar(self):
        print('O motor ligou.')

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        print('O carro está ligado.')
        self.motor.ligar()

carro = Carro()
carro.ligar()