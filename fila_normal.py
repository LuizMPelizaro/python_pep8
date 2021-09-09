from fila_base import FilaBase


class FilaNormal(FilaBase):
    # -> significa que ele retona um tipo , no caso ele nao retorna nada .
    # Mas poderia retorna uma String ,int e etc.
    def gerasenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendido.append(cliente_atual)
        return f'Cliente atual: {cliente_atual} , dirija-se ao caixa: {caixa}'
