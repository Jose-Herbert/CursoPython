'''
Operação Ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
'''
# valor condicional
# interessante para utilizar em diversas ocasiões
import os
condicao_while = True

while condicao_while:
    num_input = input('Adivinhe o número proposto: ')

    try:
        if num_input == 'clear':
            os.system('clear')

        condicao = 10 == int(num_input)
        variavel = f'Você acertou, o número era: 10' if condicao else 'Você não acertou o numero proposto...'
        
        if condicao:
            condicao_while = False

        print(variavel)
        
    except ValueError:
        # Erro de Valor.
        print('Porfavor Digite Apenas Números Inteiros')