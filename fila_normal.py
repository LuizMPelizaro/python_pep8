from fila_base import FilaBase

from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    # -> significa que ele retona um tipo , no caso ele nao retorna nada .
    # Mas poderia retorna uma String ,int e etc.
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendido.append(cliente_atual)
        return f'Cliente atual: {cliente_atual} , dirija-se ao caixa: {caixa}'
