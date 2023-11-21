class Carrinho:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    # COMPOSICAO
    def adicionar_produto(self, nome: str, preco: float) -> None:
        self._produtos.append(Produto(nome, preco))

    # AGREGACAO
    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for p in produtos:
            self._produtos.append(p)

    def listar_produtos(self):
        print()
        for p in self._produtos:
            print(f"{p.nome} - {p.preco:.2f}")
        print()


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto("Caneta", 1.50), Produto("Notebook", 21.0)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
