import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segmento:
    def __init__(self, ponto1, ponto2):
        self.pontos = Ponto(ponto1, ponto2)
        
    def calcular_comprimento(self):
        comprimento = math.dist(self.pontos.x * 2 - self.pontos.x * 1) * 2 + (self.pontos.y * 2 - self.pontos.y * 1) * 2
        print(f'A distância entre os pontos 1: {self.ponto1} e 2: {self.ponto2} é: \n{comprimento}')

pontos = Segmento(2, 4)
pontos.calcular_comprimento()


