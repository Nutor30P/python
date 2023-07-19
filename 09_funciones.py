#funciones#

#definir una funcion
def mi_funcion():
    print("hola mundo")
    print("hola mundo")
    print("hola mundo")

#llamar a la funcion
mi_funcion()

print("------------------------------------")

#definir una funcion con parametros

def mi_funcion(nombre):
    print(f"hola {nombre}")

mi_funcion("jose")

print("------------------------------------")

#definir una funcion con parametros por defecto

def mi_funcion(nombre="jose"):
    print(f"hola {nombre}")

mi_funcion()

print("------------------------------------")

#difinir funcion con return

def suma(num1, num2):
    return num1 + num2


print(suma(5, 7))

print("------------------------------------")

#llamar una funcion desde otra funcion

def suma_dos():
    suma(5, 7)

suma_dos()
