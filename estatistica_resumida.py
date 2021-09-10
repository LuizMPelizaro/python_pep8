from typing import List, Dict, Union


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> int:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: list[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {
            f'{self.agencia}-{self.dia}': len(clientes_atendidos)
        }

        return estatistica
