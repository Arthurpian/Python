# Criar uma matrix com numeros aleatorios
import random

def cria_matrix(linhas,colunas):
    matrix = []
    for i in range(linhas):
        matrix.append([])
        for j in range(colunas):
            matrix[i].append(random.randint(0,10))
    return matrix


def cria_matriz_1(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(random.randint(1, 1))  # Caso queira so com números 1
    return matriz


lista = cria_matrix(5,5)
print(lista)



