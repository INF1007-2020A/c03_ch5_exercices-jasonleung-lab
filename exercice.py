#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    Mon_numbre = float(imput('entrer un nombre: '))
    if Mon_numbre < 0:
        Mon_numbre = -Mon_numbre
    return Mon_numbre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    resultat = []
    for prefixes in prefixes:
        nom = prefixes + suffixes 
        resultat.append(nom)
    return resultat


def prime_integer_summation() -> int:
    s = 0
    n = int(input("Valeur de n"))
    For i in range (0, 100)
    s = s + i
    return s


def factorial(number: int) -> int:
    result = 1
    if number == 0:
        return result
    else:
        for i in range (number):
            result *= (number - i)
        return result
    for i in range (1, number):
        number *= (number - i )
    return number


def use_continue() -> None:
    for chiffre in range(1,11):
        if chiffre == 5:
            continue
      print (chiffre)


def main() -> None:
    #print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    #print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    #print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    #print(f"L'affichage de la boucle est:")
    #use_continue()


if __name__ == '__main__':
    main()
