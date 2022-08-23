from random import choice

palabras = ['hola','como','estas','secreto','mirada','ferrocarril','tigre']
# print(palabras)
vidas = 6
jugar = True
indices_adivinados = {}

def obtiene_palabra_secreta(p):
    palabra_secreta = []
    for index,letra in enumerate(p):
        # print(index,letra)
        palabra_secreta.append(letra)
    return palabra_secreta

def decir_numero_de_vidas(vidas):
    print(f'Tienes {vidas} vidas para adivinar la palabra.\n')

def decir_bienvenida(vidas):
    print("Hola, este es el juego del ahorcado")
    decir_numero_de_vidas(vidas)

def imprimir_palabra_escondida(palabra_secreta, letra , indices_adivinados ):
    palabras = ''
    adivino = False
    # print(palabra_secreta)
    for index,l in enumerate(palabra_secreta):

        if(letra != None and l == letra):
            palabras += ' '+letra+' '
            indices_adivinados[index] = letra
            adivino = True
        else:
            if indices_adivinados is not None and palabra_secreta[index] in indices_adivinados.values():
                palabras += ' ' + palabra_secreta[index] + ' '
            else:
                palabras += ' _ '

    print(palabras)
    return [indices_adivinados,adivino]

def verificar_si_adivino(palabra_secreta,indices_adivinados):
    return len(palabra_secreta) == len(indices_adivinados)


palabra_secreta = obtiene_palabra_secreta(choice(palabras))
# cuenta_lista = len(list({1:'holo'}.keys()))
# print(cuenta_lista)
# print(palabra_secreta)
decir_bienvenida(vidas)
imprimir_palabra_escondida(palabra_secreta, None, None)

while(jugar == True):
    # print(f'indices_adivinados {indices_adivinados}')
    letra = input('Por favor ingresa una letra: ')
    resultado = imprimir_palabra_escondida(palabra_secreta, letra, indices_adivinados)
    # print(resultado)
    if resultado[1] == False:
        vidas = vidas - 1
        print(f'Erraste te queda {vidas} vidas!...')
    indices_adivinados = resultado[0]
    # print(list(indices_adivinados))
    if verificar_si_adivino(palabra_secreta, indices_adivinados):
        print('Excelente, adivinaste la palabra es:')
        print(''.join(palabra_secreta))
        jugar = False

    if vidas == 0:
        print('Lo siento se han acabo las vidas, perdiste!')
        jugar = False

