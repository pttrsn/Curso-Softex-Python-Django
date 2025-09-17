class Cachorro:
    def __init__(self, nome, cor: str) -> None:
        self.nome = nome
        self.cor = cor
    
    def latir(self):
        print(f'{self.nome} diz: Au Au!')

meu_cachorro = Cachorro('Rex', 'Preto')

#nome e cor são atributos da 'classe Cachorro', por isso são chamadas sem parênteses.
print(meu_cachorro.nome)
print(meu_cachorro.cor)
meu_cachorro.latir()