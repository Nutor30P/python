## Condicionales ##

my_condition = True

if my_condition:
    print("La condición es verdadera")


print("Fin del programa")

# Operadores de comparación
# == igual
# != diferente
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que

my_number = 5

if my_number < 3:
    print("El número es menor que 3")
elif my_number > 3:
    print("El número es mayor que 3")


# Operadores lógicos
# and
# or
# not

my_number = 5

if my_number > 3 and my_number < 10:
    print("El número es mayor que 3 y menor que 10")

if my_number > 3 or my_number < 4:
    print("El número es mayor que 3 o menor que 4")

if not my_number == 4:
    print("El número no es 4")


# Operadores de identidad
# is
# is not

my_list_1 = [1, 2, 3]

my_list_2 = [1, 2, 3]

my_list_3 = my_list_1

if my_list_1 is my_list_2:
    print("Las listas son iguales")
else:
    print("Las listas son diferentes")

if my_list_1 is my_list_3:
    print("Las listas son iguales")
else:
    print("Las listas son diferentes")

if my_list_1 == my_list_2:
    print("Las listas son iguales")

if my_list_1 == my_list_3:
    print("Las listas son iguales")

    