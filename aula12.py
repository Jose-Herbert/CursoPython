# Formatação Strings Com Method Format()
a = 'a'
b = 'b'
c = 1.1
# Dentro da chaves pode usar os indexes da tupla format(0, 1, 2)
formato = 'a= {0} b= {1} c= {2:.2f}'.format(a, b, c)
# Dentro da função tem como nomear um parametro
formato = 'a= {nome0} b= {nome1} c= {nome2:.2f}'.format(nome0=a, nome1=b, nome2=c)

print(formato)