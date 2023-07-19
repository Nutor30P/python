## bucles ##

# bucle while
# while condicion:
#   bloque de instrucciones
#   actualizacion de contador

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("------------------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

print("------------------------------------")

# bucle for 

resultado = 0

for contador in range(0, 10):
    print("Voy por el: " + str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")

print("------------------------------------")

# Ejemplo tablas de multiplicar

numero_usuario = int(input("¿De que numero quieres la tabla?: "))
print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")

print("------------------------------------")

# Ejemplo calculadora

print("### CALCULADORA ###")

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
operacion = input("Introduce la operacion a realizar (suma, resta, multiplicacion, division): ")

if operacion == "suma":
    print(f"El resultado de la suma es: {numero1 + numero2}")
elif operacion == "resta":
    print(f"El resultado de la resta es: {numero1 - numero2}")
elif operacion == "multiplicacion":
    print(f"El resultado de la multiplicacion es: {numero1 * numero2}")
elif operacion == "division":
    print(f"El resultado de la division es: {numero1 / numero2}")
else:
    print("Operacion no contemplada")

print("------------------------------------")

# Ejemplo tabla de multiplicar con bucle for

for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")

print("------------------------------------")

# Ejemplo tabla de multiplicar con bucle while

numero_usuario = int(input("¿De que numero quieres la tabla?: "))
print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

contador = 1

while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("Tabla finalizada")


print("------------------------------------")

# Ejemplo tabla de multiplicar con bucle while y break

numero_usuario = int(input("¿De que numero quieres la tabla?: "))
print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

contador = 1

while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")

    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break

    contador += 1

else:
    print("Tabla finalizada")


print("------------------------------------")


# Ejemplo tabla de multiplicar con bucle while y continue

numero_usuario = int(input("¿De que numero quieres la tabla?: "))
print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

contador = 1

while contador <= 10:
    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break

    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1

else:
    print("Tabla finalizada")


print("------------------------------------")

# for in diccionario

print("### Ejemplo diccionario ###")

diccionario = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Colombia": "Bogota",
    "Mexico": "Ciudad de Mexico"
}

for pais, capital in diccionario.items():
    print(f"{capital} es la capital de {pais}")

print("------------------------------------")

# Ejemplo for in lista

print("### Ejemplo lista ###")

paises = ["Argentina", "España", "Colombia", "Mexico"]

for pais in paises:
    print(pais)

print("------------------------------------")