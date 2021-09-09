from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    """Utilizando o Pep8"""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendido.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str):
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.clientes_atendido)}
        else:
            estatistica = {'dia': dia,
                           'agencia': agencia,
                           'clientes_atentididos': self.clientes_atendido,
                           'quantidade_cliete_atendido': (
                               len(self.clientes_atendido)
                           )}
        return estatistica
