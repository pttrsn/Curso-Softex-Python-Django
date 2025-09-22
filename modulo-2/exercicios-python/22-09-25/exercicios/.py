'''
Objetivo: Criar uma classe com validações simples nos setters para tipo e valor. 
●  Requisitos: 
x 1.  Crie uma classe Pessoa com os atributos protegidos _nome e _idade. 
2.  Crie uma @property para nome. 
3.  Crie um @nome.setter que valide se o valor é uma string e não está vazio. 
4.  Crie uma @property para idade. 
5.  Crie um @idade.setter que valide se a idade é um número inteiro e positivo. 
6.  No __init__, use os setters para atribuir os valores iniciais (ex: self.nome = nome). 
7.  Instancie um objeto Pessoa com dados válidos e depois tente alterar nome para um 
valor vazio e idade para um valor negativo para testar as validações.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade