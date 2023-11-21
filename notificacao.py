from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        pass


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print("E-mail: enviando - ", self.mensagem)


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print("SMS: enviando - ", self.mensagem)


n = Notificacao("Testando notificação")
ns = NotificacaoSMS("Testando not")
ns.enviar()

# n.enviar()
