#Criar um tabuleiro de Xadrez
import random
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        #print(matriz)
        for j in range(colunas):
            matriz[i].append(random.randint(0,10))
        #print(matriz)
    return matriz


#Mostrar como se fosse em Xadrez
def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return


xadrez = cria_matriz(8,8)

#Aqui o I = Linha e J = Coluna, entao vai pegar um por uma linha e somar os indicis i = 0 + j=0 = 0 par i = 0 + j= 1 impar
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if (i+j)%2 == 0:
            xadrez[i][j] = 0
        else:
            xadrez[i][j] = 1

mostra_matriz(xadrez)