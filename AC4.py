'''
Matéria: Programação Estruturada - AC4
Aluno: Gabriel Rosa Barreto de Araújo

'''

#====================================================================================================================================================================================


# Exercicio 1 - AC4
print(20*"=")
print('\nExercicio 1\n')

def e_primo(num):
    
    primo = True
    for div in range(2, num):
    
        
        if num % div == 0: #  Ele retorna o resto da divisão do operando da esquerda pelo operando da direita.
            # Ele é usado para obter o resto de um problema de divisão.
            primo = False
            print(f'Não sendo primo, o {num} é divisível por {div}.\n')
             
    print(f'É primo? {primo}\n')

e_primo(7)
e_primo(14)

#====================================================================================================================================================================================


# Exercicio 02 - AC4.
print(20*"=")
print('\nExercicio 2\n')

def determina_juros(parcelas, divida):
   
    if parcelas == 1:
        return (divida)
        
    elif parcelas == 3:
        return ((3 * divida) / 100)
        
    elif parcelas == 6:
        return ((6 * divida) / 100)
    
    elif parcelas == 9:
       return ((9 * divida) / 100)
    
    elif parcelas == 12:
        return ((12 * divida) / 100)
        
def determina_parcelas(divida):
    opcoes_de_parcela = float(input('\nEm quantas vezes voce deseja parcerlar: '))
    juros = determina_juros(opcoes_de_parcela, divida)
    valor_total = divida + juros
    valor_parcela = valor_total / opcoes_de_parcela
    
    print(f' \nO valor dos juros foram: {juros:.1f}\n')
    print(f' \nO valor total: {valor_total:.1f}\n')
    print(f' \nQuantidade de parcelas: {opcoes_de_parcela:.1f}\n')
    print(f' \nVoce pagara {opcoes_de_parcela:.1f} parcelas de {valor_parcela:.1f}\n')
    
    
divida = float(input('Digite sua divida: '))
determina_parcelas(divida)
    
#====================================================================================================================================================================================

# Exercicio 03 - AC4.
print(20*"=")
print('\nExercicio 3\n')

def num_positivos():
    
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0

    
    while True:
        numero = float(input('\nDigite um número: '))
        
        if numero > 0:
            print(f'\nO número {numero} é maior que 0.\n')
            print(20*"=")
            
        else:
            print(f'\nO numero {numero} e negativo.\nEncerrando Programa...')
            break
        
        if 0 <= numero and numero <= 25:
            contador1 += 1
        elif 26 <= numero and numero <= 50:
            contador2 += 1
        elif 51 <= numero and numero <= 75:
            contador3 += 1
        elif 76 <= numero and numero <= 100:
            contador4 += 1

    print(f'\nNúmeros no intervalo de 0 a 25: {contador1}')
    print(f'\nNúmeros no intervalo de 26 a 50: {contador2}')
    print(f'\nNúmeros no intervalo de 51 a 75: {contador3}')
    print(f'\nNúmeros no intervalo de 76 a 100: {contador4}\n')

num_positivos()
#====================================================================================================================================================================================
