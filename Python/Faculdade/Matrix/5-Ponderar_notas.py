import random

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(0, 10))
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for i in matriz:
        print(matriz[i])

# Ponderação dos critérios (notas) com pesos
pesos = [1, 2, 3, 2, 1]

# Criação de uma matriz 5x10 de notas (5 critérios, 10 alunos)
notas = cria_matriz(5, 10)

# Lista para armazenar as médias finais
medias = []

# Calcula a média ponderada para cada aluno
for j in range(len(notas[0])):
    soma_pesos_notas = 0
    soma_pesos = 0
    for i in range(len(pesos)):
        soma_pesos_notas += pesos[i] * notas[i][j]
        soma_pesos += pesos[i]
    media = soma_pesos_notas / soma_pesos
    medias.append(media)

# Mostra as médias finais dos alunos
print(medias)