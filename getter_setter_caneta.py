class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor not in ("Vermelho", "Verde", "Amarelo"):
            raise ValueError("ValueError", "Cor inválida")
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta("Azul")
print(caneta.cor)

try:
    caneta.cor = "asd"
except ValueError as e:
    print(e)
    # if str(e) == "Cor inválida":
    # print("chegou aqui")
    caneta.cor = "Vermelho"
print(caneta.cor)
