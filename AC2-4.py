'''
Elabore uma função que receba uma variável inteira ano. 
Em seguida, retorne o resultado da expressão lógica que indica se um ano é ou não bissexto. 
Um ano é bissexto se ele é múltiplo de quatro. 
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. 
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

'''
def anobi(ano):
    return (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0)

def main():
    print('...', anobi(1995))

main()
# Exercicio 4 


