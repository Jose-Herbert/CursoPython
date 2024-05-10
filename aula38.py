'''

Calculadora com While

'''
condicao = True
while condicao:
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite um segundo número: ')
    operador = input('Digite um operador (+), (-), (*), (/): ')
    calculo = None

    while primeiro_numero == '' or segundo_numero == '':
        print("Porfavor digite dois numeros e um operador")
        primeiro_numero = input('Digite o primeiro número: ')
        segundo_numero = input('Digite um segundo número: ')
        operador = input('Digite um operador (+), (-), (*), (/): ')

    try:
        int_pri_numero = int(primeiro_numero)
        int_seg_numero = int(segundo_numero)
        if operador == '+':
            calculo = int_pri_numero + int_seg_numero
        elif operador == '-':
            calculo = int_pri_numero - int_seg_numero
        elif operador == '*':
            calculo = int_pri_numero * int_seg_numero
        elif operador == '/':
            calculo = int_pri_numero / int_seg_numero
        else:
            print('Porfavor digite um operador Disponível')
    except:
        print('Porfavor digite apenas números')

    if operador == '' or len(operador) > 1:
        print(' ')
        print('Error 014') # Erro de Operador (especifico, ocorreu um problema no operador)
        print(' ')
    elif calculo != None:
        print(f'O resultado foi : {calculo}')
    else:
        print(' ')
        print('Error 001') # Erro de calculo (geral, não especificado a um objeto)
        print(' ')

    deseja_sair = input('Deseja sair? [s]im [n]ão: ')
    print(' ')

    if deseja_sair == 'sim' or deseja_sair == 'Sim' or deseja_sair == 's' or deseja_sair == 'S':
        print('Desligando calculadora!')
        condicao = False
    else:
        pass






'''
Uma maneira alternativa ao inves de usar o try é usar o isdigit()
Da seguinte forma:

    if primeiro_numero.isdigit() and segundo_numero.isdigit():
        int_pri_numero = int(primeiro_numero)
        int_seg_numero = int(segundo_numero)
        if operador == '+':
            calculo = int_pri_numero + int_seg_numero
        elif operador == '-':
            calculo = int_pri_numero - int_seg_numero
        elif operador == '*':
            calculo = int_pri_numero * int_seg_numero
        elif operador == '/':
            calculo = int_pri_numero / int_seg_numero
        else:
            print('Porfavor digite um operador Disponível')
    else:
        print('Porfavor digite apenas números')
'''