'''

Interando strings com while

'''
#       0123456
#nome = 'Herbert' # Interáveis

#tamanho_nome = len(nome)
#contador_letras = -1

#maneira complicada
#while contador_letras < tamanho_nome:
#    contador_letras += 1
#    if contador_letras == tamanho_nome:
#        break
#    print(f'{nome[contador_letras]}*',end='')
#print('',end="\n")
#print('Acabou')

nome = 'Herbert'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
    
print(novo_nome)