"""

Introdução ao desempacotamento + tuples (tuplas)

"""
# Lista
nomes = ['Maria', 'Helena', 'Luiz']

nome1, nome2, nome3 = nomes
#nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
#nome1, nome2, = ['Maria', 'Helena', 'Luiz'] Pode causar erro de valores insuficientes para desempacotar

#para utilizar apenas um valor do pacote você pode usar o seguinte
#nome1, *_ = ['Maria', 'Helena', 'Luiz']

print(type(nomes))
print(nome2)