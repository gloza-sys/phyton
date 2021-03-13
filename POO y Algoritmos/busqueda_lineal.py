

from typing import Match
import random


def busqueda_linea(lista, objectivo):
    Match = False

    for elemento in lista:
        if elemento == objectivo:
            Match = True
            break
    return Match


if __name__ == "__main__":
    tamano_de_lista = int(input("de que tamaño sera la lista?"))
    objectivo = int(input("que numero quieres encontrar?"))

    lista = [random.randint(0, 1000) for i in range(tamano_de_lista)]
    encontrado = busqueda_linea(lista, objectivo)
    print(lista)
    print(f'el elemento {objectivo} {"esta" if encontrado else "no esta"} en la lista')
