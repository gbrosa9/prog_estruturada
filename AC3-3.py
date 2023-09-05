''''Faça um programa que calcule as raízes de uma equação do segundo grau, 
na forma ax^2 + bx + c. O programa deverá receber os valores de a, b e c e fazer as consistências,
 informando ao usuário nas seguintes situações:

Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.'''

# Exercício 3


a = float(input('Digite o valor de A: '))


if a == 0:
    print('Não é uma equação do segundo grau')
    print('Encerrando programa...')
    

else:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    delta = (b ** 2) - (4 * a * c)
    raiz1 = (-b + delta ** 0.5) / (2*a)
    raiz2 = (-b - delta ** 0.5) / (2*a)
    raiz3 = (raiz1 == raiz2)



if delta <0:
    print('A equação não possui raízes') 

print(f'O valor de delta é {delta:.2f}')

if (delta == 0):
    
    print(f'A equação possui apenas uma raíz real, sendo elas: {raiz1:.2f}')
elif (delta >= 1):
    
    print(f'Sendo assim, a equação possui duas raízes reais, sendo elas: {raiz1:.2f} e {raiz2:.2f}')





    
