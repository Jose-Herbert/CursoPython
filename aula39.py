frase = 'O python é uma linguagem de progamação' \
    'multiparadigma, ' \
    'python foi criado por Guido van Rossum'

i = 0

qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qnt_apareceu_mais_vezes_atual = frase.count(letra_atual)
    i += 1

    if letra_atual == ' ':
        i += 1
        continue

    if qnt_apareceu_mais_vezes < qnt_apareceu_mais_vezes_atual:
        qnt_apareceu_mais_vezes = qnt_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

print(frase)
print('A letra que apareceu mais vezes foi: '
      f'"{letra_apareceu_mais_vezes}" que apareceu:'
      f'{qnt_apareceu_mais_vezes}x'
)




#