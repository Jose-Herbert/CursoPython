"""
Exercicio
exiba os indices da lista

0 Maria
1 Helena
2 Luiz
"""

lista = ['marta', 'helena', 'luiz']
lista.append('joão')

indices = range(len(lista))

for ind in indices:
    print(ind, lista[ind], type(lista[ind]))