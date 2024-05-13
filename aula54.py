"""

Enumerate = enumera interáveis (índices)

"""

lista = ['Maria','João','Luiz']
lista.append('Helena')

lista_enumerada = enumerate(lista) 
# se você jogar essa variavel um enumerate ele no final apaga tudo o recomendado é usar o enumerate direto no for.

print(next(lista_enumerada))

#for item in lista_enumerada:
#    print(item)

#for item in enumerate(lista):
#    indice, nome = item
#    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('For da Tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')