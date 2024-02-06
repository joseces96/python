from abc import ABC, abstractmethod 

class Persona(ABC):
    '''Clase que representa una persona'''
    
    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre 
        self.apellido = apellido

    @abstractmethod
    def __str__(self):
        return " %s: %s, %s" % (str(self.cedula), self.apellido, self.nombre)
    
class Alumno(Persona):
    '''Clase que representa a un alumno'''
    def __init__(self, cedula, nombre, apellido, carrera):
        # llamamos al construtor de Persona
        Persona.__init__(self, cedula, nombre, apellido)
        # agregamos el nuevo atributo
        self.carrera = carrera

    def __str__(self):
        return super().__str__(), self.carrera

if __name__ == '__main__':
    #crear un objeto del tipo alumno
     alumno1 = Alumno("4534077", "Jose", "Cespedes","informatica")
     print('Alumnos')
     print(alumno1.__str__())
