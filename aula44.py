"""

Faça um jogo para o usuário adivinhar qual a palavra
secreta.
- Você vai propor uma palavra secreta qualquer
e vai dar a possibilidade para o usuário digitar
apenas uma letra.
- Qual o usuario digitar uma letra, vocễ vai oconferir
você vai conferir se a letra digitada está na palavra secreta

        - Se a letra digitada estiver na palavra secreta;
        exiba a letra;
        - Se a letra digitada não estiver na palavra secreta;
        exiba *,
Faça a contagem de tentativas do seu usário.

"""

palavra_secreta = 'colar'
letra_acertada = ''
qnt_tentativas = 0
acertou = False
acertou_letra = False

texto_1 = 'Jogo da Adivinhação'
texto_2 = '          ' \
'Você tem 5 Chances de acertar a palavra secreta; Se você errar o progama irá fechar.'
espaço = ' ' * 40
print(f'{espaço}{texto_1}{espaço}')
print(f'{texto_2}')
print(' ')

while acertou == False:
    print(' ')
    adivinhe_input = input('Adivinhe uma letra da Palavra Secreta: ').lower()

    # Código para saber se o input foi so uma letra ou se foi um digito
    if len(adivinhe_input) > 1 or len(adivinhe_input) < 0:
        print('Porfavor digite pelo menos uma letra!')
        acertou_letra = False
    elif adivinhe_input.isdigit():
        acertou_letra = False
        print('A palavra secreta contém apenas letras!')
    elif adivinhe_input == '':
        print('Porfavor digite uma letra')
    else:# Código para saber se a letra atual ta igual a da palavra secreta
        if adivinhe_input in palavra_secreta:
            acertou_letra = True
            letra_acertada += adivinhe_input
        else:
            acertou_letra = False

        # Código para quantidade de chances
        if adivinhe_input != letra_acertada and acertou_letra == False:
            qnt_tentativas += 1
            print(f'Você já tentou {qnt_tentativas}X')
        if qnt_tentativas == 4:
            print('Você so tem mais uma chance')

        # Código para printar a letra acertada
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letra_acertada:
                palavra_formada += letra_secreta
                acertou_letra = True
            else:
                palavra_formada += '*'
                acertou_letra = False
        print(palavra_formada)
        if palavra_formada == palavra_secreta:
            print(f'!!!Parabéns!!! Você Acertou a Palavra Secreta: "{palavra_formada}"')
            acertou = True
        if qnt_tentativas == 5:
            acertou = True
            print(f'Você não conseguiu acertar a palavra: {palavra_formada}')