# Ano Bissexto

ano = int(input('Digite um ano e verifique se é bissexto: '))

resultado = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 

print(resultado)

# print( True and False)
# print( True or False)
# print( not True)

