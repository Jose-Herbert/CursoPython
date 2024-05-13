"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis = índices e fatiamento
Método úteis : appens, insert, pop, del, clear, extend, +

(Create) (Read) (Update) (Delete)
 criar    ler    alterar  deletar
"""

lista = [10, 20, 30, 40]
lista.append(50) #adiciona ao final da fila um item
i = lista.pop() #deleta o ultimo item da lista
del lista[-1] #deleta um item
lista.clear() #limpa a lista
lista.insert(0, 5) #adiciona um item na lista
print(lista, i)
