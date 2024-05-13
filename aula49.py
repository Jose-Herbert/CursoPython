"""
Cuidados com dados mutáveis
 - copiado o valor (imutáveis)
 - Aponta para o mesmo valor na memória (mutável)
"""
# Variaveis mutaveis
nome = 'Herbert'
outra_variavel = nome
nome = 'jose'

# Lista Imutaveis
lista_a = ['luiz', 'maria']
lista_b = lista_a.copy() #uma maneira de copiar uma lista para outra

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)