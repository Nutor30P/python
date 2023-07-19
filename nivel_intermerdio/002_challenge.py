## challenges ##


"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

lista = [i for i in range(1,101)]

for i in lista:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    elif i % 3 == 0:

        print("fizz")

    elif i % 5 == 0:

        print("buzz")

    else:

        print(i)

""" 
Escribe una funcion que reciba dos palabras y devuelva True si son
    * anagramas, False si no lo son. Dos palabras son anagramas si
    * tienen las mismas letras, pero en diferente orden. Por ejemplo:
    * - 'roma' y 'amor' son anagramas.

"""

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word1 == word2:
        return True
    else:
        return False
    
print(is_anagram("amor", "roma"))


"""
-------------------------------------------------------------------------
escribe la succesion de fubonacci imprimiendo los 50 primeros numeros empezando desde 0

"""

def fibonacci():
    
    prev = 0 #1, 1
    next = 1 #1, 2

    for index in range(0,50):
        print(prev)  #0, 1, 1
        fib = prev + next #1, 2 , 3
        prev = next #1, 1, 2
        next = fib #1, 2 , 3


fibonacci()


"""
-------------------------------------------------------------------------

Escribe un programa que se encargue de comprobar si un numero es primo o no

"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
           return False
    return True


"""
-------------------------------------------------------------------------
crea un programa que invierta el orden de una cadena de texto

"""

def reverse_string(string):
    return string[::-1]

print(reverse_string("hola mundo"))