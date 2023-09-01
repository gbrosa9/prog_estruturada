'''Elabore uma função com as mesmas regras do exercício anterior
 porém retornando os três resultados, ao invés de exibi-los na tela.
 '''

 # Exercicio 3

def num(n1, n2, n3):
    n1 = n1 * 2 + (n2 /2)
    n2 =  ( n1 * 3 ) + n3
    n3 =  n3 ** 3
    return n1, n2, n3



def main():
    print('Os números são', num(2,4,6))

main()
    