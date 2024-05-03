# Aula sobre função input()

# Input para strings
nome = input('Qual seu nome? ')
print(f'O seu nome é {nome}')

# Input para numeros
numero_1 = int(input('Digite um numero: ')) # nesse metodo pode dar erro
numero_2 = int(input('Digite outro numero: ')) # nesse metodo pode dar erro
print(f'A soma dos dois numeros é: {numero_1 + numero_2}')

# Outra maneira de se fazer o Input para numeros
numero_3 = input('Digite um numero: ')
numero_4 = input('Digite outro numero: ') 
# Conversão após o input
int_numero_3 = int(numero_3)
int_numero_4 = int(numero_4)
print(f'A soma dos dois numeros é: {int_numero_3 + int_numero_4}') # esse metodo vai receber um input string porem o progama quebra no print()