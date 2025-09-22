class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.__preco = preco
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, valor):
        if self._verificar_valor(valor):
            self.__preco = valor
        else:
            print('Valor incorreto.')
        
    def _verificar_valor(self, valor):
        return valor >= 0
        
caneta = Produto('Caneta Azul', 2.50)
print('Primeiro Get')
print(caneta.get_preco())
print('Segundo Get')
caneta.set_preco(10)
print(caneta.get_preco())
print('Terceiro Get')
caneta.set_preco(-10)
#print(caneta.get_preco())