# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla cuántos números
# primos hay en el rango que va desde cero hasta ese número
# incluido, y va a devolverla cantidad de números primos que
# encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(numero):
    numeros_primos = []
    if numero > 2:
        numeros_primos.append(2)
        for n in list(range(3, numero + 1)):
            divisores = 0
            for nu in list(range(1, n + 1)):
                # print(f' {n}  %  {nu} =  {n % nu}')
                if n % nu == 0:
                    divisores += 1
            # print(f' divisores del {nu} -> {divisores}')
            if divisores == 2:
                numeros_primos.append(n)
        print(f'hay {len(numeros_primos)} numeros primos hasta el {numero}')
        print(numeros_primos)
    else:
        if numero == 2:
            numeros_primos.append(2)
            print(f'hay {len(numeros_primos)} numeros primos hasta el {numero}')
            print(numeros_primos)
        if numero < 2:
            print('No tiene numeros primos')
            print(0)


contar_primos(2000)

