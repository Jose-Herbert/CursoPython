'''

Flag (bandeira) - marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, indentidade)
id = indetidade

'''

condicao = False
passou_no_if = None

#nunca crie uma variavel dentro de um if e use ela fora
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print("não passou no if")
if passou_no_if is not None:
    print("não passou no if")