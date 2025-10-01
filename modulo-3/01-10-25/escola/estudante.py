from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self._notas = {} #notas:dict[str, list[float]] = {}

    def adicionar_nota(self, materia: str, nota:float):
        if materia not in self._notas:
            self._notas[materia] = []
        self._notas[materia].append(nota)

'''
estudante1 = Estudante("Carlos", 16, "2025001")

estudante1.adicionar_nota("Matemática", 9.5)
estudante1.adicionar_nota("Matemática", 8.0)
estudante1.adicionar_nota("História", 7.0)

print(f"Notas de Matemática: {estudante1._notas.get('Matemática')}")
print(f"Notas de História: {estudante1._notas.get('História')}")
print(f"Todas as notas: {estudante1._notas}")
'''