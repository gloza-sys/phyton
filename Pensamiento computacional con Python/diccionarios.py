def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    poblacion_pais = {
        "Argentina": 44938712,
        "Brazil": 210147125,
        "Colombia": 50372424
    }
    # for pais in poblacion_pais.values():
    #     print(pais)

    # print(poblacio⁄n_pais["Argentina"])

    for pais, poblacion in poblacion_pais.items():
        print(pais+" Tiene mas de "+ str(poblacion)+" habitantes")


if __name__ == "__main__":
    run()
