from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / "log.txt"


class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...

    # raise NotImplementedError("Implemente o método log")
    # ...

    def log_error(self, msg):
        return self._log("Error: %s" % msg)

    def log_success(self, msg):
        return self._log("Success: %s" % msg)


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        print("Salvando no log:", msg_formatada)
        with open(LOG_FILE, "a") as f:
            f.write(msg_formatada + "\n")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} {self.__class__.__name__}")


if __name__ == "__main__":
    # lp = LogPrintMixin()
    # lp.log_error("oi")
    # lp.log_success("Que legal")
    # lf = LogFileMixin()
    # lf.log_error("oi")
    # lf.log_success("Que legal")
    l = Log()
    l._log("oi")
