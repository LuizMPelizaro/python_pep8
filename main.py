from fabrica_de_fila import FabricaDeFila
from estatistica_detalhada import EstatisticaDetalhada

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(5))
# print(fila_teste_2.chama_cliente(1))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))

fila = FabricaDeFila.pega_fila('prioritaria')
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
print(fila.chama_cliente(5))
print(fila.estatistica(EstatisticaDetalhada('10/03/2000', 120)))
