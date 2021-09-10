from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> int:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: list[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes_atentididos'] = clientes_atendidos
        estatistica['quantidade_cliete_atendido'] = (
            len(clientes_atendidos)
        )

        return estatistica
