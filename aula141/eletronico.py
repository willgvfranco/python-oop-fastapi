from log import LogPrintMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    @property
    def nome(self):
        return self._nome

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._log_mixin = LogPrintMixin()

    def ligar(self):
        super().ligar()

        self._log_mixin.log_error("Ligado")

    def desligar(self):
        super().desligar()
