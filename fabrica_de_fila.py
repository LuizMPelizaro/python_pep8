from typing import Union

from fila_prioritaria import FilaPrioritaria
from fila_normal import FilaNormal
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaDeFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila inesistente ')
