

from typing import Match
import random

def busqueda_binaria(lista, comienzo, final, objectivo):
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objectivo:
        return True
    elif lista[medio]<objectivo:
        return busqueda_binaria(lista, medio+1,final, objectivo)
    else:
        return busqueda_binaria(lista, medio+1,medio-1, objectivo)


if __name__ == "__main__":
    tamano_de_lista = int(input("de que tamaño sera la lista?"))
    objectivo = int(input("que numero quieres encontrar?"))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objectivo)

    print(lista)
    print(f'el elemento {objectivo} {"esta" if encontrado else "no esta"} en la lista')
