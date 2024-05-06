"""
Fatiamento de String

 012345678
 Olá Mundo
-987654321

Fatiamento [i:f:p] [::]

Obs: a função len retorna a quantidade
de caracters da string

"""

variavel = 'Olá Mundo'
#corte de string
print(variavel[4:])
print(variavel[0:7])
#len contagem de string
print(len(variavel))

#     0 = inicio / len = final / 1 = passo (quantidade de letras que vai pular)
print(variavel[0:len(variavel):1])
