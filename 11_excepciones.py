## excepciones 

# try:
#     nombre = input("Cual es tu nombre: ")
#     if len(nombre) > 1:
#         nombre_usuario = "El nombre es " + nombre
#     print(nombre_usuario)
# except:
#     print("Ha ocurrido un error, mete bien el nombre")

# else:

#     print("Todo ha funcionado correctamente")

# finally:

#     print("Fin de la iteracion")

# try:

#     numero = int(input("Numero para elevarlo al cuadrado: "))

#     print("El cuadrado es: " + str(numero*numero))

# except TypeError:

#     print("Debes convertir tus cadenas a enteros en el codigo")

# except ValueError:

#     print("Introduce un numero correcto")

# except Exception as e:

#     print(type(e))

#     print("Ha ocurrido un error: ", type(e).__name__)

# finally:

#     print("Fin de la iteracion")

# try:

#     nombre = input("Introduce el nombre: ")


numberOne , numberTwo = 5, 0

try:
    print(numberOne/numberTwo)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except TypeError:
    print("No se puede dividir entre cadenas de texto")
except ValueError:
    print("Introduce un numero correcto")
#captura cualquier error
except Exception as e:
    print(type(e).__name__)
finally:
    print("Fin de la iteracion")


