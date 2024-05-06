'''

Formatação Básica de Strings

s - string
d - int
f - float

.<numero de dígitos>f
x ou X - Hexadecimal
(caracere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
!r __repr__
!s __str__
!a __ascii__
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: > 10}')
print(f'{variavel: < 5}')
print(f'{variavel: ^ 10}')
print(f'{1000.45643: .2f}')
print(f'O hexadecimal de 1555 é: {1555: X}')