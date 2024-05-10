"""

Como um For funciona ?

Interável -> str, range, etc (__iter__)
Interador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

"""

texto = iter('Hello World!') #__iter__() ele mostra o interador do objeto e o local dele na memória
texto = 'Hello World!'.__iter__() #ele mostra o interador do objeto e o local dele na memória

print(texto.__next__()) #vai intregar cada letra dentro do iterador, pode dar error de range.
print(next(texto)) #vai intregar cada letra dentro do iterador, pode dar error de range.

#####################################

texto = 'Hello World'

#  essa variavel letra vira um iterador do propio for e utilia como literal a variavel previamente definida.
#for letra in texto:

# A função do For é literalmente como um while abaixo
while True:
    try:
        iterador = iter(texto)
        #ele você cria uma variavel que usa o methodo next e transforma e um iterador
        letra = next(iterador)
        print(letra)
    #sempre que der um erro de stop interation ele da um break
    except StopIteration:
        break





    #