''''
Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela:

O salário antes do reajuste;
O percentual de aumento aplicado;
O valor do aumento;
O novo salário, após o aumento.

 Salários até R$ 280,00 (incluindo)      Aumento de 20%
 Salários entre R$ 280,00 e R$ 700,00    Aumento de 15%
 Salários entre R$ 700,00 e R$ 1500,00   Aumento de 10%
 Salários de R$ 1500,00 em diante        Aumento de 5%

'''

 # Exercício 1 

def calcular_reajuste_salarial():
    salario = float(input("Digite o salário atual do colaborador: R$ "))

    if salario <= 280:
        percentual_aumento = 20
    elif salario <= 700:
        percentual_aumento = 15
    elif salario <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = (percentual_aumento / 100) * salario
    novo_salario = salario + aumento

    # Exibir resultados
    print("\nResumo do reajuste salarial:")
    print(f"Salário antes do reajuste: R$ {salario}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {aumento}")
    print(f"Novo salário após o aumento: R$ {novo_salario}")

calcular_reajuste_salarial()


