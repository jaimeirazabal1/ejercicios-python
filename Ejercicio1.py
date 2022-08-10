def devolver_distintos(num1,num2,num3):
    '''
    Crea una función llamada devolver_distintos() que reciba 3
    integers como parámetros.
    Si la suma de los 3 numeros es mayor a 15, va a devolver el
    número mayor.
    Si la suma de los 3 numeros es menor a 10, va a devolver el
    número menor.
    Si la suma de los 3 números es un valor entre 10 y 15
    (incluidos) va a devolver el número de valorintermedio.

    :param num1: entero
    :param num2: entero
    :param num3: entero
    :return:
    '''
    lista = [num1,num2,num3]
    suma = num1 + num2 + num3;
    if suma > 15:
        return numero_mayor(*lista)
    if suma < 10:
        return numero_menor(*lista)
    if suma >= 10 and 15 >= suma:
        return numero_intermedio(*lista)

def numero_mayor(*args):
    mayor = 0
    for numero in args:
        if numero > mayor:
            mayor = numero
    return mayor

def numero_menor(*args):
    menor = args[0]
    for numero in args:
        if numero < menor:
            menor = numero
    return menor

def numero_intermedio(*args):
    mayor = numero_mayor(*args)
    menor = numero_menor(*args)
    for numero in args:
        if numero != mayor and numero != menor:
            return numero
    return None



print(devolver_distintos(5,3,2))