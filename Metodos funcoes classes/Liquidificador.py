class Liquidificador:
    def __init__(self):
        self.velocidade =0
        self.power = False

    def velocidade_A(self):
        self.power = True
        if self.power:
            self.velocidade = 1

    def velocidade_B(self):
        self.power = True
        if self.power:
            self.velocidade = 2

    def velocidade_Z(self):
        self.velocidade = 0
        self.power = 0
