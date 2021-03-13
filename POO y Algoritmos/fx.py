def f(x):

    respuesta = 0

    for i in range(1000):
        #print(i)
        respuesta += 1
    
    for i in range(x):
        #print(i)
        respuesta += x
    
    for i in range(x):
        for j in range(x):
            #print(j)
            respuesta += 1
            respuesta *= 1
    
    return respuesta

r = f(1000)
print(r)