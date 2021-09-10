import abc
from typing import List
from constantes import TAMANHO_MAXIMO_PADRAO, TAMANHO_MINIMO_PADRAO


# O metodo abc é uma classe abstrata
class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendido: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO_PADRAO:
            self.codigo = TAMANHO_MINIMO_PADRAO
        else:
            self.codigo += 1

    def insere_na_fila(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_na_fila()

    # Isso força com que a classe filha crie esse metodo
    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
