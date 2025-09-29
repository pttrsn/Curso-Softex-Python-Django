class Teclado:
    def ligar(self):
        print('O teclado está ligado.')

class Mouse:
    def ligar(self):
        print('O mouse está ligado.')

class Monitor:
    def ligar(self):
        print('O monitor está ligado.')

class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()

    def ligar_computador(self):
        self.teclado.ligar()
        self.mouse.ligar()
        self.monitor.ligar()
        print('O computador está pronto para inicialização.')

computador = Computador()
computador.ligar_computador()
