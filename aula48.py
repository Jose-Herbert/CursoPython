"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis = índices e fatiamento
Método úteis : appens, insert, pop, del, clear, extend, +

(Create) (Read) (Update) (Delete)
 criar    ler    alterar  deletar
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
lista_a.extend(lista_b) # quando um metodo não retorna nada ele mexe no valor principal
print(lista_a)