from estudante import Estudante

class Escola:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        if estudante not in self.estudantes:
            self.estudantes[estudante] = []
        self.estudantes[estudante].append(estudante)

    def mostrar_relatorio(self):
        pass

escola = Escola()
estudante1 = Estudante("Carlos", 16, "2025001")
escola.adicionar_estudante(estudante1)