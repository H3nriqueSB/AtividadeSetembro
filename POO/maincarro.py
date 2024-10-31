# carro = {
#     # "chave" : "valor",
#     "marca" : "volkswagen",
#     "modelo" : "fusca",
#     "cor" : "azul",
#     "ano" : "1945",
# }

# print(carro.get("marca"))
# print(carro.get("modelo"))
# print(carro.get("cor"))
# print(carro.get("ano"))

class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 

    def acelerar(self):
        print(f'O carro {self.modelo} acelerou')

fusca = Carro("Volkswagen", "Fusca", "Azul", 1935)
fusca.acelerar()

print(vars(fusca))