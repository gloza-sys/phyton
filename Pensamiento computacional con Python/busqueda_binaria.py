objectivo = int(input("Escoge un numero: "))
epsilon = 0.001
bajo = 0.0
alto = max(1.0,objectivo)
respuesta = (alto+bajo)/2

while abs(respuesta**2 - objectivo)>= epsilon:
    print(f'bajo={bajo}, alto ={alto}, respuesta = {respuesta}')
    if respuesta**2 < objectivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto+bajo)/2

print(f'la raiz cuadrada del {objectivo} es {respuesta}')
