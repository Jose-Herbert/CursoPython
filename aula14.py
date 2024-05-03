# if / elif / else
# se / se não se / se não

'''
para multiplas condições utilizasse o () 
e repete a condição por (1 or 2) 
ou And para multiplas condições corretas
'''
entrada = input('Você quer "entrar" ou "sair"? ')

if (entrada == "entrar" or entrada == "Entrar"):
    print("Você entrou no sistema")
elif (entrada == "sair" or entrada == "Sair"):
    print("Você saiu do sistema")
else:
    print("Você não digitou nem entrar nem sair!")