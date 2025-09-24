class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def som(self):
        print('Som!') #Método da superclasse Animal.

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def som(self):
        print('Au au!') #Método da subclasse Cachorro.


class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie

    def som(self):
        print('Miau!') #Método da subclasse Gato.
    


cao = Cachorro('Rex', 4, 'Vira-lata') #Executando a subclasse Cachorro.
print(cao.nome)
print(cao.idade)
print(cao.raca)
cao.som()

print()

gato = Gato('Félix', 3, 'Persa') #Executando a subclasse Gato.
print(gato.nome)
print(gato.idade)
print(gato.especie)
gato.som()