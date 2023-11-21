class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua: str, numero: int) -> None:
        self.endereco.append(Endereco(rua, numero))
        pass

    def listar_enderecos(self):
        for e in self.endereco:
            print(f"{e.rua} - {e.numero}")
        print()

    def __del__(self) -> None:
        print(f"Cliente {self.nome} foi deletado")


class Endereco:
    def __init__(self, rua: str, numero: int) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self) -> None:
        print(f"Endereço {self.rua} - {self.numero} foi deletado")


cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Rua ABC", 123)
cliente1.inserir_endereco("Rua XYZ", 456)
cliente1.listar_enderecos()


print("AQUI TERMINA O CÓDIGO")
