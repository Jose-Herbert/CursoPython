"""

Introdução ao try/except
try -> Tentar executar o código
except -> ocorreu um erro ao tentar executar

"""

numero = input(
    'Digite um numero para ser dobrado: '
)
# Método como try
try:
    numero_int = int(numero)
    print(f'O dobro de {numero} é {numero_int * 2}')
except:
    print('isso não é um numero')



# Método como if
#if numero.isdigit():
#    numero_int = int(numero)
#    print(f'O dobro de {numero} é {numero_int * 2}')
#else:
#    print('isso não é um numero')