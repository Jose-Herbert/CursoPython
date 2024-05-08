'''

Faça um progama que peça ao usuario para digitar um número inteiro,
informe-se este número é par ou impar. caso o usuário não digite um numero
inteiro, informe que não é um número inteiro.

'''
num_int_input = input('Digite um número inteiro: ')

try:
    par_ou_impar = int(num_int_input) % 2 == 0
    if par_ou_impar:
        print(f'Seu número {num_int_input} é um número Par')
    else:
        print(f'Seu número {num_int_input} é um número Impar')
except:
    print('Você não digitou um número Inteiro')






'''

Faça um progama que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação adequada. EX:
Bom Dia 00-11; Boa Tarde 12-17 e Boa Noite 18-23

'''
hora_input = input('Digite que horas são: ')

if hora_input.isdigit():
    int_hora = int(hora_input)
    if int_hora <= 11:
        print('Bom Dia')
    elif int_hora <= 17:
        print('Boa Tarde')
    elif int_hora <= 23:
        print('Boa Noite')
    else:
        print('Porfavor digite uma hora entre 0 e 23 horas;')
        print('De acordo com o Horario de Brasília')
else:
    print('Vocẽ não digitou uma hora')




'''

Faça um progama que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos escreva('seu nome é curto'); 
se tiver entre 5 e 6 letras, escreva('seu nome é normal'),
 maior que 6 escreva('seu nome é muito grande')

'''
nome_input = input('Digite seu Nome: ')
len_nome = len(nome_input)

if len_nome == 0:
    print('Você não digitou nada')
elif len_nome <= 4:
    print('Seu nome é curto')
elif len_nome == 5 or len_nome == 6:
    print('Seu nome é normal')
elif len_nome > 6:
    print('Seu nome é muito grande')
