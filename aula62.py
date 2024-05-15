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
import os

cpf_correto = False
resultado_1 = 0
resultado_2 = 0

# enquanto cpf não estiver completo e tiver faltando
# letra vai ficar rodando o loop
while cpf_correto == False:
    print(' ' * 5, 'Analisador de CPF')
    print('Digite seu CPF: ')
    cpf_input = input('') \
    .replace('.', '') \
    .replace(',', '') \
    .replace('-', '') \

        # para caso o usuário digite um cpf sequencial de mesmo número
    entrada_sequencial = cpf_input == cpf_input[0] * len(cpf_input)
    if entrada_sequencial:
        print('Entrada sequencial não aceita!')
        print('')
        print('Fechando Sistema...')
        cpf_correto = True

    try:
        razao = 10
        # se o input for um digito e o tamanho desse input for 11 digitos ele irá limpar o console
        # printar um header e fazer o calculo
        if cpf_input.isdigit() and len(cpf_input) == 11:
            os.system('clear')
            print('Analisando CPF')
            print('...')
            print('')

            # For para o primeiro digito
            # para cada digito no input ele ira adicionar o resulado com um inteiro do digito * a razão que é 10 pois é uma PA
            for digito_cpf in cpf_input[:9]:
                resultado_1 += (int(digito_cpf) * razao)
                razao -= 1

            # resultado do primeiro digito é o resultado da soma de todos os digitos * a razão
            resultado_primeiro_digito = resultado_1 * 10 % 11


            # se o resultado do primeiro digito tiver no input ele irá prosseguir para o calculo do segundo digito
            if str(resultado_primeiro_digito) in cpf_input:
                # For para o segundo digito
                # nesse for ele irá repetir o mesmo processo porém adicionando o resultado do primeiro digito
                razao = 11
                for digito_cpf in cpf_input[:10]:
                    resultado_2 += int(digito_cpf) * razao
                    razao -= 1

                # resultado do segundo digito é o resultado da soma de todos os digitos + o primeiro digito * a razão
                resultado_segundo_digito = resultado_2 * 10 % 11
            
            # se o resultado do primeiro não tiver no input esse cpf é invalido
            else:
                print('CPF Invalido')

        # se essa afirmação for falsa (if cpf_input.isdigit() and len(cpf_input) == 11:)
        # ele irá limpar o console e pedir para você digitar tudo novamente
        else:
            os.system('clear')
            print('Porfavor digite o cpf corretamente!!')
            print('')

        cpf_formado = f'{cpf_input[:9]}{resultado_primeiro_digito}{resultado_segundo_digito}'
        # se o cpf formado for igual ao input ele irá fechar o laço
        if cpf_formado in cpf_input:
            print(f'Seu CPF É: {cpf_input[:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{resultado_primeiro_digito}{resultado_segundo_digito}')
            print('')
            print('Seu CPF Está Validado')
            print('')
            print('Fechando sistema...')
            cpf_correto = True
        else:
            print('!!!Seu CPF É Invalido!!!')
            print('')
            print('Fechando sistema...')
            cpf_correto = True


# Exeções de erros (depois documentar)
    except ValueError:
        print('Error 105 ValueError...')
        print('')
        print('Porfavor Digite um CPF Valido')

    except TypeError:
        print('Error 067 TypeError...')
        print('')
        print('Porfavor Digite um Valor Valido')

    except NameError:
        print('Error 217 NameError...')
        print('')
        print('Porfavor Digite Apenas Números')










'''
 todos os digitos do cpf vão ser direcionados ao cpf formado
cpf_formado.append(digito_cpf)

                
 outro append na lista de cpf formado so que convertendo para str o resultado do primeiro digito
cpf_formado.append(str(resultado_primeiro_digito))
print(cpf_formado)


 outro append na lista de cpf formado so que convertendo para str o resultado do segundo digito
cpf_formado.append(str(resultado_segundo_digito))
print(cpf_formado)
'''