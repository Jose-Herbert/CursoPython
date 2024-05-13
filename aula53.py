"""

Tipo tupla - Uma lista imutável

"""
#Tupla sem parenteses
nome = 'Maria', 'Helena', 'Luiz' # não pode alterar valores
#Tupla com parenteses
nome = ('Maria', 'Helena', 'Luiz') # não pode alterar valores

#da para converter uma tupla para lista e vice-versa
nome = tuple(nome)
print(type(nome))
nome = list(nome)
print(type(nome))

print(nome[0])
print(nome)