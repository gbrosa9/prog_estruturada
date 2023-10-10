""" 
Programação Estruturada

10/10/2023
Estruturas de Dados

Listas e Tuplas
"""

# Construção de listas
alunos = ["abc", "def", "ghi"]
lista = [1, 4.5, False, [1,2,3,]] # Não é uma boa prática.

# Acesso a elementos
print(alunos[1])
# print(alunos[3]) -> erro de indice
print(alunos[-1]) # ultimo elemento da lista

# Matrizes
coordenadas = [
    [ 2,  6],
    [ 1, 10],
    [-1, -5]
]
print(coordenadas[0][1])

matriz_3d = [
    [
        [1,2],
        [3,4]
    ],
    [
     [5,6],
     [7,8]
    ]
]
print(matriz_3d[1])
print(matriz_3d[1][0])
print(matriz_3d[1][0][1])

# Slicing
print("-" * 40)
alunos = ["abc", "def", "ghi", "jkl", "mno", "pqr"]
print(alunos[1:5])          # range (start, stop, step)
print(alunos[1:6:2]) 
print(alunos[:4:2])  # Começa no inicio da lista
print(alunos[1::2]) # Termina no final da lista
print(alunos[1:])  # Do primeiro elemento de indice 1, até o último elemento.
print(alunos[::-1]) # Inverte a lista

# Operações com listas - Pertencimento
print("-" * 40)
print("def" in alunos) # Retorna True ou False
print("stu" in alunos) # Retorna um booleano, ou seja, True ou False, se tem "stu" na estrutura
print("stu" not in alunos) 

# Operações com listas - Soma
print([1, 2] + [3, 4])  # Vai retornar [1, 2, 3, 4]

# Operações com listas - Multiplicação  #
print([0] * 10) # Vai retornar [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Operações com listas - Iteração
print("-"* 40)
for aluno in alunos:
    print(aluno)

for indice, aluno in enumerate(alunos): # Enumarete serve pra juntar os elementos (abc, def) com os indices (0,1,2)
    print(indice, aluno, sep =" - ") # Retornar os indices.. 0 - abc, 1 - def..

notas = [7.5, 6.5, 8.2, 4.8, 6.4, 2.3]
for nota, aluno in zip(notas, alunos):  # Zip é para quando quer percorrer duas listas ao mesmo tempo.
    print(aluno, nota, sep=": ")

# não é uma boa prática -> não é pythonico
for indice in range(len(alunos)):
    print(alunos[indice])
    

# Funções e Métodos com listas
print("-" * 40)
print(len(alunos))

alunos.append("stu") # append serve pra adicionar um elemento no final de uma lista.
print(alunos)


alunos.insert(3,"vwx")  # da pra definir o indice que você quer adicionar alguma elemento, por exemplo o vwx.
print(alunos) # retornara -> ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu']


alunos.extend(["yza", "bcd"]) # vai acrescentar os 2 elementos dessa lista.
print(alunos)

print("-" * 40)
print(alunos.pop()) # Remove o último elemento da lista e RETORNA o elemento removido,
# e retorna o elemento atualizado.
print(alunos.pop(3))
print(alunos)

# print(alunos.remove(1)) # Precisa colocar o indice que quer remover (2) <- remove o indice 2.
print(alunos.remove("jkl")) # Remove a primeira ocorroência do elemento JKL.
print(alunos)

if "jkl" in alunos: # Caso contrário, pode subir um erro de valor.
    alunos.remove("jkl")

print(alunos.index("mno"))

alunos = [ "abc", "def", "abc", "abc"]
print(alunos.count("abc")) # Conta quantas ocorrências tem dentro da lista, no caso ali tem 3.

print(max(notas)) # Imprime a maior nota
print(min(notas)) # Imprime a menor nota
print(sum(notas)) # Pode dar erro com floats.

print(notas)
notas.sort() # Ordena a lista notas do menor para o maior.
print(notas)

notas_ord = sorted(notas) #retorna uma nova lista, ordena a lista inplace
print(notas_ord)


# Compreensão de listas ; List comprehension
print("-" * 40)
numeros = [1,2,3,4,5,6,7]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

print(quadrados)

quadrados2 = [numero **2 for numero in numeros]  # É melhor USAR dessa maneira.
print(quadrados2)

quadrado_impar = [numero ** 2 for numero in numeros if numero % 2 ==1]
print(quadrado_impar)

# Dados mutáveis vs. Imutáveis

print("-" * 40)
x = 2
y = x
x = 3
print(x, y)

a = [1]
b = a 
a.append(2)
a[0] = 999
print(a,b)

def limpa_dados(lista, valor_a_limpar):
    for dado in lista:
        if dado == valor_a_limpar:
            lista.remove(dado)


nomes = ["a", "b", "c", "a", "a", "d", "a"]
novos_nomes = nomes.copy() # Vai gerar uma nova lista, em outro espaço da memória.
limpa_dados(novos_nomes, "a")
print(nomes)
print(novos_nomes)

print("-" * 40)
def adiciona_elemento(elem, lista=None):
    if lista is None:
        lista = []
    lista.append(elem) # Appendi inclui um elemento, nesse caso esta incluindo o elemento.
    return lista 

a = [1,2,3]
adiciona_elemento(4, a)
adiciona_elemento(5, a)
adiciona_elemento(6, a)
print(a)

b = adiciona_elemento(8) # [8]
print(b)
b = adiciona_elemento(7) #[7]
print(b)



    


# Tuplas -> Lista imutáveis
print("-" * 40)
tupla = (1,2,3,4,5)
print(tupla)
print(tupla[2])
print(tupla[0])
print(tupla[0:2])

def informa_nomes():
    nome1 = input("Informe um nome: ")
    nome2 = input("Informe um nome: ")
    return nome1, nome2
nomes = informa_nomes()
print(nomes)
print(type(nomes))


primeiro_nome, segundo_nome = informa_nomes()
print(primeiro_nome, "- ", segundo_nome)
