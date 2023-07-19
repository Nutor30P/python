## class ##

#definiendo una clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años")

    def despedir(self):
        print("Adios, me voy")

#instanciando la clase

Persona1 = Persona("Juan", 28)

Persona1.saludar()

Persona1.despedir()

#herencia

class Estudiante(Persona):
    def __init__(self, nombre, edad, escuela):
        Persona.__init__(self, nombre, edad)
        self.escuela = escuela

    def saludar(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años y estudio en", self.escuela)
              

Estudiante1 = Estudiante("Juan", 28, "UNAM")

Estudiante1.saludar()


#polimorfismo

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Guau, guau")

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Miau, miau")

def escuchar_mascota(mascota):
    mascota.ladrar()

perro = Perro("Firulais")
gato = Gato("Misifu")

escuchar_mascota(perro)
escuchar_mascota(gato)



#encapsulamiento

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()
    
ejemplo = Ejemplo()

print(ejemplo.atributo_publico())

ejemplo.metodo_publico()

