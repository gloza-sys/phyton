def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos "+ tipo_pesos +" tienes? ")
    pesos = float(pesos)
    valor_dolar = int(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print ("Tienes $"+ dolares + " Dolares") 

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Argentinos
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argeninos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)

else:
    print("Ingresa una opcion correcta por favor")


