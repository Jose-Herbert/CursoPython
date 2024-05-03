'''
Operadores Lógicos
# and (e) or (ou) not (não)
...................................................
.and - todas as condições precisam ser verdadeiras.
.Se qualquer valor for falso a expressão inteira  .
.Será considerada falsa                           .
...................................................
'''
primeira_senha = input('Digite sua senha de entrada: ')
print("Você Deseja Fazer Login ?")
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = primeira_senha
if entrada == 'E' and senha_digitada == senha_permitida:
    print('(Usuário Logado)')
elif entrada == 'S':
    print('(Usuário Deslogado)')
elif entrada == 'E' and senha_digitada != senha_permitida:
    print('Senha incorreta')
else:
    print('(Login Negado)')