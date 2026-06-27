

import random


liste_5000 = [random.randint(1, 100) for _ in range(5000)]

pairs = [x for x in range(20) if x % 2 == 0]

# print(f"Voici la liste aléatoire des 5000 entiers : {liste_5000}")

print(f"Voici la liste des valeurs paires inferieurs à 20 : {pairs}")

def safe_divide(a: float, b: float) -> float | None:
    """Divise a par b, retourne None si division par zéro."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Erreur : division par zéro impossible.")
        return None
    
test_division = safe_divide(25, 0)
print(f"La réponse est : {test_division}")

# Exercice sur la compréhension des listes et les erreurs


import random


def filter_even_squares(numbers: list[int]) -> list[int]:
    """Fonction qui retourne le carré de chaque nombre paire de la liste, en une seule ligne de comprehension liste"""
    
    resultat = [x**2 for x in numbers if x % 2 == 0]
    return resultat


def safe_get_average(numbers: list[int]) -> float | None:
    """Une fonction qui calcule la moyenne d'une liste"""

    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("Erreur :  La liste est vide")
        return None
    

def main() -> None:
    """Fonction principale servant à tester les autres fonctions"""

    listes_a_tester = {
        "liste vide" : [],
        "liste singleton" : [6],
        "liste longue" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "liste aleatoire" : [random.randint(1, 50) for _ in range(26)]
    }

    for nom, liste in listes_a_tester.items():
        print(f"--- Test avec la {nom}")
        print(f"Carrés des pairs : {filter_even_squares(liste)}")
        print(f"Moyenne : {safe_get_average(liste)}")
        print()

if __name__ == "__main__":
    main()