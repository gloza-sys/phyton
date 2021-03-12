

class persona:
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola  {otra_persona.nombre}, me llamo {self.nombre}'
    
    def edades(self, otra_persona):
        return f'Hola  {otra_persona.nombre}, me llamo {self.nombre} y tengo {self.edad} años'


david = persona("David", 35)
erika = persona("Erika", 32)

david.saluda(erika)
david.edades(erika)
