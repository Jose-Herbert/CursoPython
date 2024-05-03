nome = input("Digite Seu Nome: ")
altura = float(input("Digite Sua Altura Em Metros: "))
peso = float(input("Digite Seu Peso em Kg: "))

imc = float(peso) / float(altura)**2
print(" ", end='\n')
#"f-strings" Strings Formatadas

linha_1 = f'Altura: {altura:.2f}'
linha_2 = f'Peso: {peso:.1f}'
linha_3 = f'Seu IMC É: {imc:.2f}'

print(f'Nome: {nome}')
print(linha_1)
print(linha_2)
print(linha_3)