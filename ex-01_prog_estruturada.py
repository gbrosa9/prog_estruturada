# Através de Fórmula de BHASKARA.

print('Olá, sejam bem vindos!')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C '))

delta = (b ** 2) - 4 * a * c


numero1 = (-b + delta ** (1 / 2)) / (2 * a)
numero2 = (-b - delta ** (1 / 2)) / (2 * a)

print(f'As raizes são {numero1:.2f} e {numero2:.2f}')


# Fórmula de BHASKARA -> x = (-b ± √(b² – 4ac)) / (2a)











