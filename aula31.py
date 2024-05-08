'''

https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos: string(str), integrer(int), float(float), boolean(bool).

'''

string = 'Herbert'

#zfill
print(string.zfill(10))


















'''
string = input('Digite um numero ')
#string2 = input('Digite um minutos ')
hora_primaria = string[0:2]
hora_segundaria = string[2:len(string)]
#minutos = string[2:5]
try:
    hora_int = int(hora_primaria)
    if hora_int >= 00 or hora_primaria <= 11:
        print(f'Bom Dia! {hora_primaria}{hora_segundaria}')
    elif hora_int >= 12 or hora_primaria <= 17:
        print(f'Boa Tarde! {hora_primaria}{hora_segundaria}')
    elif hora_int >= 18 or hora_primaria <= 23:
        print(f'Boa Noite! {hora_primaria}{hora_segundaria}')
    else:
        print('Digite uma hora no padrão 12:00')
except:
    if string == None:
        print('Você não digitou um numero')
'''