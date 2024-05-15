"""
Desempacotamento em chamadas
de métodos e funçõess
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python', 'é', 'legal')

# em uma lista você pode desempacotar cada index em uma variavel
""" p, s, *_, ap, u = lista
print(p, u, ap) """

print(*lista) 
# é a mesma coisa que 
print('Maria', 'Helena', 1, 2, 3, 'Eduarda')

print(*string)
print(*tupla)


# desempacotar lista separando por sep no print

salas = [
    # 0      # 1
    ['Maria', 'Helena', ], # 0
    
    # 0
    ['João', ], # 1

    # 0     # 1       # 2         # 3
    ['Luiz', 'Arthur', 'Eduarda', (0, 10, 20, 30, 40)], # 2
]    

print(*salas, sep='\n')