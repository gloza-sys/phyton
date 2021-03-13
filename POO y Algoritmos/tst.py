

def funcion_decoradora(funcion_parametro):
    
    def funcion_interior(*args, **kwargs):

        #acciones adicionales que decoran
        print("Vamos a realizar un calculo:")
        funcion_parametro(*args, **kwargs)
        
        #acciones adicionales que decoran
        print("Hemos terminado el calculo")

    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

def potencia(base, exponente):
    print(pow(base,exponente))

suma(7,5,8)
resta(12,10)

potencia (base=5,exponente=3)

















# class Departamentos:
#     def __init__(self, precio):
#         self._precio = precio        #atributo privado
    
#     @property
#     def precio(self):#cuando se ejecute departamento.precio
#         return self._precio         #retornar el atributo privado _precio
    
#     @precio.setter                  #setter, se ejecutará cuando se intente cambiar los valores
#     def precio(self, nuevo_valor):  
#         if nuevo_valor < 1000 or nuevo_valor > 200000:  #si valor es menor a 1000 o mayor a 200000
#             raise ValueError('No es posible cambiar a estos valores')   #arrojamos error
#         else:                                          
#             self._precio = nuevo_valor                  #asignamos el nuevo valor
#             print(f'El nuevo valor del departamento es: {self._precio}')    #imprimimos el nuevo valor
    
#     @precio.deleter                 #supersor
#     def precio(self):
#         del self._precio            #borramos el atributo

# casa_playa = Departamentos(60000)

# casa_playa.precio = 80000

# del casa_playa.precio