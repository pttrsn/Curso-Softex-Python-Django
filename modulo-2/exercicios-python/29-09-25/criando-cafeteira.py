class GraoDeCafe:
    def moer(self):
        print("Os grãos de café foram moídos.")

class Agua:
    def aquecer(self):
        print("A água está aquecida.")

class Cafeteira:
    def __init__(self):
        self.grao_de_cafe = GraoDeCafe()
        self.agua = Agua()
    
    def preparar_cafe(self):
        self.grao_de_cafe.moer()
        self.agua.aquecer()
        print('Café pronto.')

cafeteira = Cafeteira()
cafeteira.preparar_cafe()
