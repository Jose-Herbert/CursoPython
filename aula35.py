'''

Repetições

while(enquanto)
Executa a função enquanto uma condições for verdadeira.
loop infinito -> quando um código não tem fim

'''

contador = 0

#loop com fim
while contador < 100: #ele para no numero 10
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 30:
        print('Não vou mostrar o ', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('acabou')