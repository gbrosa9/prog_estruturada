"""
Programação Estruturada

10/10/2023

Estrutura de Dados
- Conjuntos
    - Mutáveis
    - Não oordenados
    - Únicos
    - Não suporta indexação
- Dicionários (Mapas)
    - Mutáveis
    - Não oordenados
    - Únicos
    - Suportam indexação por chaves imutáveis

"""

numeros = [1,8,5,1,2,6,1,2,8,4,3]
numeros_unicos = set(numeros)  # set remove todos os dados duplicados e fornece de forma crescente
numeros_unicos.add(9) # Adiciona o numero 9 na lista
print(numeros_unicos)



outros_numeros = set()
outros_numeros.add(3)
outros_numeros.add(8)
outros_numeros.add(7)
outros_numeros.add(3)
print(outros_numeros)

outros_numeros.remove(7) # Remove o elemento 7.
print(outros_numeros)

numeros = list(set(numeros)) # Remove os dados repetidos.
print(numeros)





print("-" * 40)




# aluno = { chave: valor }

aluno = {
    "nome": "Victor",
    "matricula": "123456",
    1.45: 45,
    False: 10,
    (1,2): "sem sentido"
}
print(aluno["nome"])
print(aluno["matricula"])
print(aluno[False])
# print(aluno["matrícula"]) -> gera KeyError

print(aluno.get("matrícula", "Erro! Chave não identificada.")) # Get verifica se o dado existe ou não

aluno = {
    "nome": "Victor",
    "matricula": "123456",
    "curso": "Engenharia de computação",
    "disciplinas": [
            {
            "nome_disciplina": "Programação",
            "cód": "IBM1737",
            "notas": {
                "ap1": 7.5,
                "ap2": 8.2,
                "ac": 4.5
            }
        },

         {
            "nome_disciplina": "Cálculo",
            "cód": "IBM1738",
            "notas": {
                "ap1": 8.2,
                "ap2": 6.4,
                "ac": 9.4
            }
        }

    ]
}
print(aluno["disciplinas"][0]["cód"])

print("-" * 40)
for chave in aluno: # Itera sobre as chaves de um dicionário.
    print(chave)

print("-" * 40)
for chave in aluno.keys(): # Mesma coisa.
    print(chave)

print("-" * 40)
for valor in aluno.values(): # Itera sobre os valores de um dicionário.
    print(valor)

    
print("-" * 40)
for chave, valor in aluno.items(): # Itera sobre as chaves de um dicionário.
    print(chave, "-" , valor)

# Adicionando elemento
aluno["data_nasc"] = "10/10/2000"
print(aluno)


# Removendo chaves
if "discipinas" in aluno:
    aluno.pop("disciplinas")
print(aluno)