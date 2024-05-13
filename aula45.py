"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis = índices e fatiamento
Método úteis : appens, insert, pop, del, clear, extend, +
"""

#         01234
#        -54321
string = "ABCDE"
lista = [123, True, 'ABCD']


#print(bool(lista)) # Se a lista estiver vazia ela é considerada falsa
#print(lista,type(lista))

#         0     1     2   
lista = [123, True, 'ABC']
#        -3    -2    -1
# Você pode mudar uma variavel dentro de uma lista acessando o index dela
lista[2] = 'Hello World!'
print(lista[2].upper(), type(lista[2]))
