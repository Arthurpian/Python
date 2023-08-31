#Printa todos os elemtos da lista
def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return


lista = [1,2,3],[4,5,6],[7,8,9]

printa_elementos(lista)