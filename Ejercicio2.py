def reducir_lista(lista_numeros):
    repetidos = {}
    nueva_lista = []
    for numero in lista_numeros:
        if repetidos.get(numero) != None:
            repetidos[numero] = repetidos[numero] + 1
        else:
            repetidos[numero] = 1
            nueva_lista.append(numero)

    indice_del_mas_alto = nueva_lista.index(obtener_mas_alto(nueva_lista))
    nueva_lista.pop(indice_del_mas_alto)
    return nueva_lista


def promedio(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero

    return suma/len(lista_numeros)

def obtener_mas_alto(lista):
    alto = 0
    for numero in lista:
        if(numero > alto):
            alto = numero
    return alto

lista_numeros = [1,4,6,8,6,23,7,2,74,2,8,6]
# [1,4,6,8,23,7,2]
lista = reducir_lista(lista_numeros)
print(lista)

# dicci = {'a':1}
# print(dicci.get(1))