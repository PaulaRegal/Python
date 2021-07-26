class ArCondicionado:
    def __init__(self):
        self.temperatura = 20

    def aumentarTemperatura(self):
        if self.temperatura < 30:
            self.temperatura += 1

#o ar não seja regulado menor que 18 graus
    def diminuirTemperatura(self):
        if self.temperatura > 18:
            self.temperatura -= 1

arCondicionado = ArCondicionado()
arCondicionado.aumentarTemperatura()
print('Temperatura atual: {}'.format(arCondicionado.temperatura))
arCondicionado.diminuirTemperatura()
print('Temperatura atual: {}'.format(arCondicionado.temperatura))
arCondicionado.diminuirTemperatura()
print('Temperatura atual: {}'.format(arCondicionado.temperatura))
arCondicionado.diminuirTemperatura()
print('Temperatura atual: {}'.format(arCondicionado.temperatura))
arCondicionado.diminuirTemperatura()
print('Temperatura atual: {}'.format(arCondicionado.temperatura))