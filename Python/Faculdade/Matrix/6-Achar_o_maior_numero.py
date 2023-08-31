lista = [ 1,2,5,6,2,3,14 ]

maior = 0

for i in lista:
    if maior < i:
        maior = i
    else:
        maior = maior

print(maior)


#Chat Gbt
maior_valor = max(lista)
indice_maior = lista.index(maior_valor)
print("O maior valor na lista é:", maior_valor)
print("O maior valor está no índice:", indice_maior)


def achar_maior(lista):
    maior=lista[0]
    indice_maior= 0
    for i in range(len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i
    return maior , indice_maior


maior_na_lista = achar_maior(lista)
print(maior_na_lista)