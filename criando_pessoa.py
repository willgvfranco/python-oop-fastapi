import json
import os


CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), "bdpersonagens.json")
# print(CAMINHO_ARQUIVO)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print("oi", args, kwargs)

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 27)
p3 = Pessoa("Pedro", 11)
bd = [vars(p1), p2.__dict__, vars(p3)]
#
# p1.metodo_de_classe()


martinha = Pessoa.criar_com_50_anos("Marta")
# print(vars(martinha))
# Pessoa.metodo_de_classe()

Pessoa.funcao_que_esta_na_classe(1, 2, 3)
p1.funcao_que_esta_na_classe(4, 5, 6)


def fazendo_dump():
    with open(CAMINHO_ARQUIVO, "w") as arq:
        json.dump(bd, arq, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    fazendo_dump()
