'''
Lista dentro de lista e seus Índices
'''

salas = [
    # 0      # 1
    ['Maria', 'Helena', ], # 0
    
    # 0
    ['João', ], # 1

    # 0     # 1       # 2         # 3
    ['Luiz', 'Arthur', 'Eduarda', (0, 10, 20, 30, 40)], # 2
]                                # 0  1   2   3   4

print(salas[0][1]) # Helena
print(salas[2][2]) # Eduarda
print(salas[2][3][2]) # Busca o 20 da tupla dentro da lista