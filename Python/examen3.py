"""from funcionesExamen import *

cadena = input("ingrese una cadena de caracteres:\n")
sin_repetidos = palabras_sin_caracteres_repetidos(cadena)
if sin_repetidos:
    print(", ".join(sin_repetidos))
else:
    print("No hay palabras sin caracteres repetidos en la cadena.")


cadena = input("ingrese una cadena de caracteres:\n")
palabra = input("ingrese un de caracter:\n")
palabras_filtradas = filtrar_palabras_por_vocales(cadena, palabra)
if palabras_filtradas:
    print("Las palabras donde la longitud de sus vocales es mayor a la longitud de vocales de la palabra introducida son:")
    for palabra_filtrada in palabras_filtradas:
        print(palabra_filtrada)
else:
    print("No se encontraron palabras donde la longitud de sus vocales es mayor a la longitud de vocales de la palabra introducida")



cadena =input("ingrese una cadena de caracteres:\n")
print(palindromo_mas_largo(cadena))"""



vector1 = {1, 2, 3}
vector2 = {3, 4, 5}

union = vector1.union(vector2)

print(union)



def interseccion(vector1, vector2):
    nuevovector = []
    for elemento in vector1:
        if elemento in vector2:
            nuevovector.append(elemento)
    return nuevovector


vector1 = [1, 2, 3, 4, 5]
vector2 = [4, 5, 6, 7, 8]
resultado = interseccion(vector1, vector2)
print(resultado)



primervector = {1, 2, 3, 4, 5}
segundovector = {4, 5, 6, 7, 8}

nuevovector = primervector.difference(segundovector.difference)

print(nuevovector)





