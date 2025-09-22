'''
Objetivo: Usar um setter para validar dados numéricos e ter métodos que usam a property. 
●  Requisitos: 
x 1.  Crie uma classe Circulo com um atributo protegido _raio. 
x 2.  Crie uma @property para raio. 
x 3.  Crie um @raio.setter que valide se o valor do raio é um número positivo. 
4.  Crie um método calcular_area() que use a propriedade self.raio para retornar a área 
do círculo (A=π⋅r2). 
5.  Instancie um círculo, teste a alteração do raio para um valor válido e um inválido, e 
imprima a área.
'''

from math import pi
#Forma alternativa import math -> use math.py

class Circulo:
    def __init__(self, raio: float):
        self._raio = raio

    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, raio_enc: float):
        if isinstance(raio_enc, float) and not raio_enc < 0:
            self._raio = raio_enc
        else:
            print('Erro! O valor do raio deve ser um número positivo.')
    
    def calcular_area(self):
        pass
