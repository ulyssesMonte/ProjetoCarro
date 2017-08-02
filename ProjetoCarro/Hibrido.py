from Carro import Carro

class Hibrido (Carro):
    def __init__ (self,cor,modelo,ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def CarregarBateria (self):
        print("Carregando bateria")
