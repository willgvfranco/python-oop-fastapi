from criando_pessoa import CAMINHO_ARQUIVO, Pessoa, fazendo_dump
import json


fazendo_dump()

with open(CAMINHO_ARQUIVO, "r") as arq:
    dados = json.load(arq)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

with open(CAMINHO_ARQUIVO, "r") as arq:
    pessoas = [Pessoa(**dado) for dado in json.load(arq)]


pass
