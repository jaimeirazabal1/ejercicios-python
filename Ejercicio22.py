# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido"
# , debería devolver ['d'
# ,
# 'e'
# ,
# 'i'
# ,
# 'n'
# ,
# 'o'
# ,
# 'r'
# ,
# 't']

def cualquiera(palabra):
    repetidas = {}
    palabra = list(palabra)
    nueva = []
    for letra in palabra:
        if repetidas.get(letra) is None:
            nueva.append(letra)
            repetidas[letra] = 1
        else:
            repetidas[letra] = 1
    nueva.sort()
    return nueva

print(cualquiera('entretenido'))