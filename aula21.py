'''
Operadores Lógicos
# in e not in
..........................................................
. Strings são interáveis
.
. 0 1 2 3 4 5 6
. h e r b e r t
.-7-6-5-4-3-2-1
..........................................................
'''
nome = 'herbert'
#print(nome[2])
#print(nome[3])
print(nome)
#in
print('is a in nome?')
print(' a' in nome)
print('is e in nome?')
print(' e' in nome)
print(20 * '-')
#not in
print('is a not in nome?')
print(' a' not in nome)
print('is e not in nome?')
print(' e' not in nome)

digite_nome = input('Digite um nome: ')
encontrar = input('Digite letras para encontrar: ')

if encontrar in digite_nome:
    print(encontrar,' está em nome: ', digite_nome)
else:
    print(encontrar,' não está em nome: ', digite_nome)
