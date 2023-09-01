'''Elabore uma função que receba três números e exiba na tela: 
(1) o produto do dobro do primeiro com metade do segundo; 
(2) a soma do triplo do primeiro com o terceiro; 
(3) o terceiro elevado ao cubo'''

# Exercicio 2

def num(n1, n2, n3):
    n1 = n1 * 2 + (n2 /2)
    n2 =  ( n1 * 3 ) + n3
    n3 =  n3 ** 3
    return n1, n2, n3



def main():
    print('Os números são', num(2,4,6))

main()
    