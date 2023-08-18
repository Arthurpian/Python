"""""
nota = int(input('Diga seu nota: '))

if nota <= 4 :
    print("Você e burro")
elif nota <= 6:
    print("Voce esta quase lá.")
else:
    print("Voce passou")
"""""
"""""
senha = "1234"
senha_usuario = input("Diga sua senha: ")
i= 0

while not senha_usuario == senha and i <= 2:
    print("errou")
    senha_usuario = input("Diga sua senha: ")
    i+=1

if senha_usuario == senha:
    print("Logado")
else:
    print("Sai hacker")
"""""
"""""
lista = [1,25,2369,1178,1858,2189]
for elem in lista:
    print(elem)
"""""
"""""
nome = "Danilo"
for char in nome:
    print(char)
"""""
"""""
lista = [1,25,2369,1178,1858,2189]
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
"""""
"""""
lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0

for elem in lista:
    soma += elem

print(soma)
media = soma/len(lista)
print(media)
"""""
"""""
lista_1 = [1,2,4,5,7,8]
lista_2 = [3,2,6,5,9,8]
repe = 0
for elem in lista_1:
    for elem_1 in lista_2:
        if elem == elem_1:
            repe+=1
print(repe)
"""""
"""""
nome = [ ]
print(nome)
nome.append("Danilo")
print(nome)
"""""
"""""
lista = [ ]
qtd = int(input("Quantos nomes você quer colocar: "))c
valor = 0

while valor < qtd:
    names = input("Digite o nome: ")
    lista.append(names)
    valor+=1

print(lista)
"""""
"""""
lista = [ ]
qtd = int(input("Quantos nomes você quer colocar: "))
for i in range(qtd):
    nome = input(f"Diga o {i+1} nome: ")
    lista.append(nome)
print(lista)
"""""
"""""
lista = [0,0,1,0,1,1]
sequencia = [1,0,1]
teste = False

for i in range(len(lista)-len(sequencia)+1):
    if lista[i] == sequencia[0]:
            for k in range(1, len(sequencia)):
                if lista[i+k] != sequencia[k]:
                    break
                if k == len(sequencia)-1:
                    teste = True
if teste:
    print("Exite")
else:
    print("Não existe")
"""""
"""""
lista = [12,2,3,5,32235,363,2596000]

def achar_maior(numeros):
    indice_maior = 0
    maior = numeros[indice_maior]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
            indice_maior = i
    return indice_maior

indice_maior_elemento = achar_maior(lista)
print(indice_maior_elemento)
print(lista[indice_maior_elemento])
"""""
"""""
matriz = [[1,2,3],[423,5,6],[5,2332,90000]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])
"""""
"""""
import numpy as np
matriz = [1,2,3],[423,5,6],[5,2332,90000]
matriz = np.array(matriz)
print(matriz)
"""""
def printa_matriz(matriz):
    for i in range(len(matriz)):
         print(matriz[i])
    return

def marta ( linha,coluna ):
    matriz=[]
    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            matriz[i].append(0)
    return matriz

def soma_matriz(matriz1,matriz2):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            matriz1[i][j] = matriz1[i][j]+matriz2[i][j]
    return matriz1

def troca (matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)//2+1):
            aux = matriz[i][j]
            matriz [i][j]  = matriz[j][i]
            matriz[j][i] = aux
        return matriz

"""""
Zerar a lista

matriz=[[1,2,3],[4,5,6],[7,8,9]]
def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz)
    return 
matriz_1=[[1,2,3,10],[4,5,6,11],[7,8,9,12]]
for i in range(len(matriz_1)):
    for j in range(len(matriz_1[1])):
        matriz_1[i][j]= 0
printa_matriz(matriz_1)
"""""
matriz = [ [12,22,32,42,52],[15,24,39,48,57],[12,21,33,42,51],[11,21,32,41,55],[10,20,30,40,50]]
"""""
printa_matriz(matriz)
for j in range(1, len(matriz[0]),2):
    print(f"Coluna indice {j}")
    for i in range(len(matriz)):
        print(matriz[i][j])

for i in range(0, len(matriz),2):
    print(f"Linha {i}")
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
"""""
"""""                                                                                            for i in range(len(matriz)):
    print(" "*4*i, end=" ")
    print(matriz[i][i])
"""""
"""""  
matriz_1 = marta(10,10)
for i in range(len(matriz_1)):
    for j in range(len(matriz_1[0])):
        if i == j :
            matriz_1[i][j] = 1
printa_matriz(matriz_1)

import matplotlib.pyplot as pit
pit.imshow(matriz_1, "hot")
pit.colorbar()
pit.show()
"""""
matriz1 = [9,8,7],[6,5,4],[3,2,1]
matriz2 = [1,2,3],[4,5,6],[7,8,9]
"""""  
soma = soma_matriz(matriz1,matriz2)
printa_matriz(soma)
"""""
"""""  
matriz1 = [9,8,7],[6,5,4],[3,2,1]
printa_matriz(matriz1)
print()
matriz1_transposta = troca(matriz1)
printa_matriz(matriz1_transposta)
"""""
matr = marta(6,6)
for i in range(len(matr)):
    for j in range(len(matr)):
        if i % 2 == 0:
            if j % 2 == 0:
                matr[i][j] = 1
            else:
                matr[i][j] = 0
        else:
            if j % 2 == 0:
                matr[i][j] = 0
            else:
                matr[i][j] = 1
                
printa_matriz(matr)
'''
def msotra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def criar(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

lista = criar(10,10)

for i in range(len(lista)):
    for j in range(i+1,len(lista)):
            lista[i][j] = 2

msotra_matriz(lista)

print()

for i in range(len(lista)):
    for j in range(i,len(lista[0])):
        aux = lista[i][j]
        lista[i][j] = lista[j][i]
        lista[j][i] = aux

msotra_matriz(lista)
'''
pesos = [1,2,3,2,1]
alunos = criar(5,10)
soma_pesos = 9
notas = []

for j in range(len(alunos[0])):
    soma = 0
    for i in range(len(pesos)):
        soma+= pesos[i] * alunos [i][j]
    soma/= soma_pesos
    notas.append(soma)
print(notas)
def msotra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def criar(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz


lista = criar(10,10)
'''
lista_2 = criar(10,10)

for i in range(len(lista)):
    for j in range(len(lista[0])):
        if j % 2 == 0:
            lista[i][j] = 1



for i in range(1, len(lista_2), 2):
    for j in range(len(lista_2)):
            lista_2[i][j] = 2

msotra_matriz(lista)
print()
msotra_matriz(lista_2)
'''
for i in range(len(lista)):
    for j in range(len(lista[0])):
        if i%2 == j%2:
            lista[i][j] = 0
        else:
            lista[i][j] = 1
msotra_matriz(lista)


