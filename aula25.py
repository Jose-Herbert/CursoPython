'''

Ecercício
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade foram digitados:
    Exiba:
        Seu nome é
        Seu nome invertido é
        se nome contem ou não espaços
        seu nome tem (n) letras
        a primeira letra do seu nome é (letra)
        a ultima letra do seu nome é (letra)
Se nada for digitado em nome ou idade:
    exiba "Desculpe, Você deixou o campo vazio"

'''

var_nome = input('Digite seu nome: ')
var_idade = input('Digite sua idade: ')
nome = str(var_nome)
qtd_esp = ' ' in nome

if var_nome != '' or var_idade != '':
    #nome normal
    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {var_idade}')
    #nome invertido
    print(f'Seu nome invertido é: {nome[len(nome)::-1]}')
    #quatidade de espaços
    if qtd_esp == 0 :
        print('Seu nome não contem espaços')
    else:
        print(f'Seu nome contem: {qtd_esp}')
    #quantidade de letras
    print(f'Seu nome tem: {len(nome)} letras')
    #a primeira letra do seu nome é
    print(f'A primeira letra do seu nome é: {var_nome[0]}')
    #a ultima letra é
    print(f'A ultima letra do seu nome é: {var_nome[-1]}')
else:
    print('Desculpe, Você deixou os campos vazios')