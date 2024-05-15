"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import sys
import random

cpf_finalizado = False
resultado_1 = 0
resultado_2 = 0
qnt_max_num_cpf = '123456789' # essa variavel serve apenas para dizer como deve ser o padrão do cpf
cpf_gerado = ''

# enquanto cpf não estiver completo
# vai ficar rodando o loop
while cpf_finalizado == False:
    print(' ' * 5, 'Gerador de CPF 5000!!!')
    razao = 10

    # esse for é apenas para a criação do cpf e para conceatenação do cpf
    for digito in qnt_max_num_cpf:
        digito_cpf = random.randint(0, 9)
        cpf_gerado += str(digito_cpf)


    # esse for faz a soma e multiplicação do cpf para obter o primeiro digito 1
    for num in cpf_gerado[:9]:
        resultado_1 += (int(num) * razao)
        razao -= 1

    resultado_primeiro_digito = resultado_1 * 10 % 11
    
    if resultado_primeiro_digito > 9:
        resultado_primeiro_digito = 0
        cpf_gerado += str(resultado_primeiro_digito)

    else:
        cpf_gerado += str(resultado_primeiro_digito)


    # esse for faz a soma e multiplicação do cpf para obter o primeiro digito 1
    razao = 11
    for num in cpf_gerado[:10]:
        resultado_2 += (int(num) * razao)
        razao -= 1

    resultado_segundo_digito = resultado_2 * 10 % 11

    print(f'Seu CPF Gerado É: {cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{resultado_primeiro_digito}{resultado_segundo_digito}')
    print('')
    print('Seu CPF Está Validado')
    print('')
    print('Fechando sistema...')
    cpf_correto = True
    cpf_finalizado = True