# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False
def funcion(*args):
    for index, numero in enumerate(args):
        if numero == 0 and len(args) > index + 1 and args[index + 1] == 0:
            return True
    return False


print(funcion(5, 6, 1, 1, 1, 9, 1, 0))


