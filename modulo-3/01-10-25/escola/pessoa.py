class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    
'''    
    @nome.getter
    def nome(self, valor):
        if isinstance(valor, str) and valor:
            self._nome = valor
        else:
            raise ValueError('O nome deve conter apenas letras.')
'''