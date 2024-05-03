nome = input("Digite Seu Nome: ")
altura = float(input("Digite Sua Altura Em Metros: "))
peso = int(input("Digite Seu Peso em Kg: "))

imc = int(peso) / float(altura)**2
print(" ", end='\n')
print('Nome: ', nome)
print('Altura: ', altura)
print('Peso: ', peso)
print('Seu IMC É De: ', imc)