# class Automovil:

#     def __init__(self, modelo, marca, color) -> None:
#         self.modelo = modelo
#         self.marca = marca
#         self.color = color
#         self._estado = "En reposo"
#         self._motor = Motor(cilindros=4)

#     def acelerar(self, tipo="despacio"):
#         if tipo == "rapida":
#             self._motor.inyecta_gasolina(10)
#         else:
#             self._motor.inyecta_gasolina(3)
#         self._estado = "En movimiento"


# class Motor:

#     def __init__(self, cilindros, tipo='gasolina') -> None:
#         self.cilindros = cilindros
#         self.tipo = tipo
#         self._temperatura = 0

#     def inyecta_gasolina(self, cantidad):
#         pass

class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo                        #atributo público 
        self.marca = marca                          #atributo público
        self.color = color                          #atributo público
        self._estado = 'en_reposo'                  #atributo privado
        self._motor = Motor(cilindros = 4)          #atributo privado, el atributo _motor es un objeto de la clase
        self._radio = Radio()

    menus =[""" 
    ---------- ¿Qué deseas hacer? ----------
    1.- Acelerar Despacio
    2.- Acelerar Rapido
    3.- Usar radio
    4.- Salir del auto
    
    Digite una opción -->  """ ,
    """                            
                       | 
                       | 
         .============.| 
       |-RADIO VOCHIDO--|.
       | [_________I__] |
       |  "(P)  (>) (<) |
       | .=====..=====. |
       | |:::::||:::::| |
       | '=====''=====' |
       '----------------' 
       OPCIONES:
       X = Cambiar canal [USB/RADIO]
       P = Play/Stop
       S = Siguiente
       A = Anterior
       E = Salir de la radio
       
       Digita una opción -> """ ,
       """                            
                       |    |~/
                       |   _|~
         .============.|  (_|   |~/
       |-RADIO VOCHIDO--|.     _|~
       | [_________I__] |     (_|
       |  "(P)  (>) (<) |
       | .=====..=====. |
       | |:::::||:::::| |
       | '=====''=====' |
       '----------------' 
       OPCIONES:
       X = Cambiar canal [USB/RADIO]
       P = Play/Stop
       S = Siguiente
       A = Anterior
       E = Salir de la radio
       
       Digita una opción -> """ ,
       """
       ---------- AUTOMOVIL -----------
       OPCIONES:
       X = Cambiar canal [USB/RADIO]
       P = Play/Stop
       S = Siguiente
       A = Anterior
       E = Salir de la radio
       
       Digita una opción -> """]         #creo una lista menu, en donde el indice 0 es el menu para el auto y el 1 para la radio

    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapido':                         #si el tipo de aceleración es rapida
            self._motor.inyecta_gasolina(10)        # que el objeto motor inyecte mas gasolina
        else:
            self._motor.inyecta_gasolina(3)         # que el objeto motor inyecte poca gasolina

        self._estado = 'en_movimiento'              # cambiamos el atributo estado por: en_movimiento
    
    def radio(self):
        while True:
            if self._radio.reproductor == 'si':
                canal_radio = self.menus[2]         #Eligo el menu a mostrar, cuando se reproduce o no
            elif self._radio.reproductor == 'no':
                canal_radio = self.menus[1]

            opcion = input(canal_radio)

            if opcion == 'X':
                if self._radio.canal == 'radio_frecuencia':
                    self._radio.cambiar_canal('usb')
                else:
                    self._radio.cambiar_canal()
                    
            elif opcion == 'P':
                if self._radio.reproductor == 'si':
                    self._radio.reproducir(estado='no')
                else:
                    self._radio.reproducir()
            elif opcion == 'S':
                self._radio.siguiente()
            elif opcion == 'A':
                self._radio.retrotroceder()
            else:
                break


class Motor:                               #crear una clase Motor 
    
    def __init__ (self, cilindros, tipo = 'gasolina'):   # el parametro: tipo -> es un parametro por defecto o default keyword
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        print(f'Acelerando, una cantidad de {cantidad}')
    
class Radio:                                #clase radio, las instancias de la clase podran: encender(), cambiar_canal(), reproducir(), siguiente(), retroceder()
    
    def __init__(self, canal = 'radio_frecuencia',estado = 'apagado'):
        self.canal = canal
        self.estado = estado
        self.reproductor = 'no'    
    def encender(self):
        self.estado = 'encendido'
    
    def cambiar_canal(self, tipo_de_canal='radio_frecuencia'):
        
        if tipo_de_canal == 'usb':
            self.canal = 'usb'
            print('    --- Se ha cambiado al USB --- ')
        else:
            self.canal = 'radio_frecuencia'
            print('    ---Se ha cambiado al RADIO FRECUENCIA ---')
    def reproducir(self, estado = 'si'):

        if estado == 'no':
            self.reproductor = 'no'
        else:
            self.reproductor = 'si'
            
    
    def siguiente(self):
        print('>>>>> Sigiente música >>>>>>')
    
    def retrotroceder(self):
        print('<<<<< Musica anterior <<<<<<<')



def run():                      
    
    vochido = Automovil('sapito','volkswagen','negro')      #instancia de la clase Automovil: creo un objeto de nombre vochido que es de clase Automovil
    
    while True:                         #hago un bucle, en donde simpre me va estar mostrando el menu y
        opcion = int(input(vochido.menus[0]))   #cuando el usuario introdusca valores que no estan dentro del if
        if opcion == 1:                 #salgo termino el bucle y se cierra el programa
            vochido.acelerar()
        elif opcion == 2:
            vochido.acelerar('rapido')
        elif opcion == 3:
            vochido.radio()
        else:
            break
    
    

if __name__ == '__main__':          #entry point
    run()                           #función inicial