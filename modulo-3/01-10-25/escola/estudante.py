from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    notas:dict[str, list[float]] = {}

    def adicionar_resultado(materia: str, nota:float):
        aula = notas.get(materia)
        print(aula)
        if aula:
            aula.append(nota)
        else:
            notas[materia] = [nota]

        print(notas)

    adicionar_resultado('Matemática', 9.0)


'''   @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if isinstance(valor, float) and valor:
            self._nota = valor
            return self._nota
        else:
            raise ValueError('A nota deve conter apenas números.')

nota = {
    'Matemática': 9.5, 
    'Química': 7.0, 
    'Física': 7.5
}'''