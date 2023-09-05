''''
Implementa uma função que receba um número e exiba o dia correspondente da semana 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


''' 
# Exercício 2

def semana(dia):

    if dia <= 0 or dia >=8:
        print('Valor inválido') 
    elif dia == 1:
        print('Domingo')
    elif dia == 2:
        print('Segunda-Feira')
    elif dia == 3:
        print('Terça-Feira')
    elif dia == 4:
        print('Quarta-Feira')
    elif dia == 5:
        print('Quinta-Feira')
    elif dia == 6:
        print('Sexta-feira')
    elif dia == 7:
        print('Sábado')


semana(8)