'''

Repetições

while(enquanto)
Executa a função enquanto uma condições for verdadeira.
loop infinito -> quando um código não tem fim

'''

condicao = True

#loop infinito
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'seu nome é {nome}')

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'seu nome é {nome}')
    #você pode tanto deixar a condiçao falsa
    condicao = False
    #quanto usar um break para quebrar o laço
    if nome == '' or nome == 'sair':
        break