'''
Operadores Lógicos
# or (e) or (ou) not (não)
..........................................................
.or - Qualquer uma das condições precisam ser verdadeiras.
.Se qualquer valor for verdadeiro a expressão inteira    .
.Será considerada naquele valor.                         .
..........................................................
'''
primeira_senha = input('Digite sua senha de entrada: ')
print("Você Deseja Fazer Login ?")
entrada = input('[E]ntrar [S]air: ')

senha_permitida = primeira_senha
if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Digite sua senha: ')
    if senha_digitada == senha_permitida:
        print('(Usuário Logado)')
    elif senha_digitada != senha_permitida:
        print('!!Senha incorreta!!')
        print('(Usuário Deslogado)')
elif entrada == 'S' or entrada == 's':
    print('(Usuário Deslogado)')
else:
    print('(Login Negado)')


    # Avaliação de curto circuito
#And
print(True and False) # No and se tiver um Falso entre os verdadeiros ele considera apenas o falso.
#Or
print(True or False) # No or se tiver apenas uma verdadeira ele considera apenas ela.