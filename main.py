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


