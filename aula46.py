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
lista[2] = 300
print(lista)
print(lista[2])
del lista[2] # Cuidado ao apagar um indice pois pode gerar um erro de range
# evitar apagar indices de lista que tem muitos indices
print(lista)
lista.append(50) #adiciona um item no fim da lista
ultimo_valor = lista.pop() #remove o ultimo item da lista
print(lista, 'Removido ', ultimo_valor)