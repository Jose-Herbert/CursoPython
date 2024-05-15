"""
Split e join com list e str
split - divide uma string
join  - une uma string
"""
#separar palavra por palavra pelo espaço
frase = 'Olá Mundo!!'

lista_palavras = frase.split()
print(lista_palavras)

#separar pela virgula
frase_2 = 'Olá mundo, Novamente!!'

lista_frase = frase_2.split(',')


#usando for no split
for i, frase_2 in enumerate(lista_frase):
    print(lista_frase[i].strip())

print(lista_frase)

#join
frases_unidas = ', '.join(lista_frase)
print(frases_unidas)