"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

"""
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_fibonacci_number(num):
    is_square = math.isqrt(5 * num * num + 4) ** 2 == (5 * num * num + 4) or \
                math.isqrt(5 * num * num - 4) ** 2 == (5 * num * num - 4)
    return is_square

def is_even(num):
    return num % 2 == 0

def check_number_properties(num):
    is_prime_result = is_prime(num)
    is_fibonacci_result = is_fibonacci_number(num)
    is_even_result = is_even(num)

    properties = []

    if is_prime_result:
        properties.append("primo")
    else:
        properties.append("no primo")
    if is_fibonacci_result:
        properties.append("fibonacci")
    else:
        properties.append("no fibonacci")
    if is_even_result:
        properties.append("par")
    else:
        properties.append("impar")

    return properties

# Ejemplo de uso
number = int(input("Ingrese un número: "))
number_properties = check_number_properties(number)
print(f"{number} es {', '.join(number_properties)}")
