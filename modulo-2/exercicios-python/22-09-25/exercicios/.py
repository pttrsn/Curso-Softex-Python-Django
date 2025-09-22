'''
Objetivo: Criar uma classe com validações simples nos setters para tipo e valor. 
●  Requisitos: 
x 1.  Crie uma classe Pessoa com os atributos protegidos _nome e _idade. 
x 2.  Crie uma @property para nome. 
x 3.  Crie um @nome.setter que valide se o valor é uma string e não está vazio. 
x 4.  Crie uma @property para idade. 
x 5.  Crie um @idade.setter que valide se a idade é um número inteiro e positivo. 
x 6.  No __init__, use os setters para atribuir os valores iniciais (ex: self.nome = nome). 
x 7.  Instancie um objeto Pessoa com dados válidos e depois tente alterar nome para um 
valor vazio e idade para um valor negativo para testar as validações.
'''

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome_enc:str):
        if isinstance(nome_enc, str) and not nome_enc == '': 
            self._nome = nome_enc
        else:
            print('Erro! O nome deve ser uma string não vazia.')
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade_enc:int):
        if isinstance(idade_enc, int) and not idade_enc < 0:
            self._idade = idade_enc
        else:
            print('Erro! A idade deve ser um valor inteiro e não negativo.')




pessoa_enc = Pessoa('João', 27)
print(pessoa_enc.nome)
print(pessoa_enc.idade)

pessoa_enc.nome = 'Rogério'
pessoa_enc.idade = 34
print(pessoa_enc.nome)
print(pessoa_enc.idade)

pessoa_enc.nome = ''
pessoa_enc.idade = -10