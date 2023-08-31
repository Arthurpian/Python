import random

def criar_matrix(linha,coluna):
    matrix = []
    for i in range(linha):
        matrix.append([])
        for j in range(coluna):
            matrix[i].append((random.randint(0,0)))
    return matrix

def mostrar_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

matrix = criar_matrix(10,10)



for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:  # i < j para embaixo i > j encima
            matrix[i][j] = 1

mostrar_matrix(matrix)