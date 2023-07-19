##List##

my_list = [1, 2, 3, 4, 5]

my_list2 = list(range(1, 6))

print(my_list2)

print(my_list)

print(my_list[0])

print(my_list[0:3])

print(my_list[2:])

print(my_list[-1])

my_list[0] = 0

my_other_list = []

#lista de todo tipo de datos

my_list_all = [1, 2, 3, 4, 5, "John", 3.14, True, [1, 2, 3]]

print(my_list_all)

#cuenta cuantas veces aparece un elemento en la lista

print(my_list_all.count("John"))

#agrega un elemento al final de la lista

my_list_all.append("Smith")

print(my_list_all)

#agrega un elemento en la posicion que se le indique

my_list_all.insert(0, "Mr.")

print(my_list_all)

#agrega una lista a otra lista

my_list_all.extend(["Jr.", "III"])

print(my_list_all)


#elimina el ultimo elemento de la lista

my_list_all.pop()

print(my_list_all)


#elimina el elemento de la posicion que se le indique

my_list_all.pop(0)


#elimina el elemento que se le indique

my_list_all.remove("John")

print(my_list_all)

#elimina todos los elementos de la lista

my_list_all.clear()

print(my_list_all)

#ordena la lista

my_list = [5, 3, 1, 2, 4]

my_list.sort()

print(my_list)

#ordena la lista de forma inversa

my_list.sort(reverse=True)

print(my_list)

#ordena la lista sin modificar la original

my_list = [5, 3, 1, 2, 4]

print(sorted(my_list))

print(my_list)


#invierte la lista

my_list.reverse()

print(my_list)

#devuelve el indice del elemento que se le indique

print(my_list.index(3))

#devuelve la longitud de la lista

print(len(my_list))

#devuelve el elemento mas grande de la lista

print(max(my_list))

#devuelve el elemento mas pequeño de la lista

print(min(my_list))

#devuelve la suma de todos los elementos de la lista

print(sum(my_list))

#devuelve la lista en forma de tupla

print(tuple(my_list))