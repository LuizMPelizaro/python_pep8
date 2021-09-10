from typing import Dict, Union

from fila_base import FilaBase

from constantes import CODIGO_PRIORITARIO
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):
    """Utilizando o Pep8"""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendido.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, retorna_estatistica: Classes) -> Dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendido)
