class Fabricante:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Motor:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Carro:
    def __init__(self, fabricante: Fabricante, nome: str, motor: Motor) -> None:
        self.fabricante = fabricante
        self.nome = nome
        self.motor = motor


fiat = Fabricante("Fiat")
hp20 = Motor("HP 20")
ferrari = Carro(fiat, "Ferrari", hp20)

print(ferrari.nome)
print(ferrari.motor.nome)
print(ferrari.fabricante.nome)
