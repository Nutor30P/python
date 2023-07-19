### File Handling ###

import os

# Para abrir un fichero en Python, usamos la función open().

# Sintaxis:

# open(filename, mode)

# filename: nombre del fichero (string).

# mode: modo de apertura del fichero (string).

txt_file = open("./fichero.txt", "r+") ## r+ = lectura y escritura

#print(txt_file.read())

#print(txt_file.read(10))

for line in txt_file.readlines():
    print(line)


#txt_file.write("\nHola mundo") ## Añade al final del fichero

#os.remove("./fichero.txt") ---> Elimina el fichero

# Modos de apertura de ficheros:

# r: lectura (read).

# w: escritura (write).

# a: añadir (append).

# x: crear (create).

# t: texto (text).

# b: binario (binary).

# Ejemplo:

# txt_file = open("fichero.txt", "rt")

# Para cerrar un fichero, usamos la función close().


# Ejemplo:

# txt_file.close()

#JSON FILES

import json

# Para abrir un fichero JSON en Python, usamos la función open().

# Sintaxis:

# open(filename, mode)

# filename: nombre del fichero (string).

# mode: modo de apertura del fichero (string).

json_file = open("./fichero.json", "w+")

# Para escribir en un fichero JSON en Python, usamos la función dump().

# Sintaxis:

# json.dump(data, file)

# data: datos a escribir en el fichero (diccionario).

# file: fichero en el que escribir los datos (file).

# Ejemplo:

json_test = {"name": "John", "age": 30, "city": "New York", "lenguajes": ["Python", "Java", "C++"]}

new_json = {"name": "Pablo", "age": 20, "city": "Bogota", "lenguajes": ["Python", "Java", "C++"]}

#agregar un nuevo elemento al diccionario

json_test["lenguajes"].append("C#")

#guardar el diccionario en el fichero

json.dump(json_test, json_file)

# Para guardar el json en el fichero

json_file.close()



# Para leer un fichero JSON en Python, usamos la función load().

# Sintaxis:

# json.load(file)

# file: fichero del que leer los datos (file).

# Ejemplo:

#json_file = open("./fichero.json", "r+")

#json_data = json.load(json_file)

#print(json_data)

#contador = 0

#for key, value in json_data.items():
#    if key == "lenguajes":
 #       contador = 1
  #  print(key, value)
   # print(contador)

# Para cerrar un fichero JSON en Python, usamos la función close().

# Ejemplo:

#json_file.close()

# Para eliminar un fichero JSON en Python, usamos la función remove().

# Sintaxis:

# os.remove(filename)

# filename: nombre del fichero (string).

# Ejemplo:

# os.remove("fichero.json")

# Para comprobar si un fichero existe en Python, usamos la función exists().

# Sintaxis:

# os.path.exists(filename)

# filename: nombre del fichero (string).

# Ejemplo:

# os.path.exists("fichero.json")



# CVS FILES

import csv

# Para abrir un fichero CSV en Python, usamos la función open().

# Sintaxis:

# open(filename, mode)

# filename: nombre del fichero (string).

# mode: modo de apertura del fichero (string).

csv_file = open("./fichero.csv", "w+")

# Para escribir en un fichero CSV en Python, usamos la función writer().

# Sintaxis:

# csv.writer(file)

# file: fichero en el que escribir los datos (file).

# Ejemplo:

csv_writer = csv.writer(csv_file)

# Para escribir una fila en un fichero CSV en Python, usamos la función writerow().

# Sintaxis:

csv_writer.writerow(["Nombre", "Edad", "Ciudad"])

csv_writer.writerow(["Pablo", 20, "Bogota"])




#xlsxwriter

#.xml file
