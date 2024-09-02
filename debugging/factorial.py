#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémente n pour éviter une boucle infinie
    return result

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Veuillez entrer un nombre positif.")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
else:
    print("Veuillez fournir un nombre en argument.")