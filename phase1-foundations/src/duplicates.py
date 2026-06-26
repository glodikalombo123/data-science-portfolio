
import time
import random

def find_duplicates_naive(numbers: list[int]) -> list[int]:
    """
    Retourner la liste des valeurs dupliquées(méthode non optimisée)

    Args:
        numbers (list[int]): Liste d'entier à analyser

    Returns:
        list[int]: la liste de retour ou le resultat
    """
    duplicates: set[int] = set()

    for i in range(len(numbers)):           # Position 1, 2, 3...
        for j in range(len(numbers)):           # Position 1, 2, 3...
            if i!= j and numbers[i] == numbers[j]:
                # Position différente, mais même valeur -> doublon trouvé
                duplicates.add(numbers[i])
    return list(duplicates)

def find_duplicates_optimized(numbers: list[int]) -> list[int]:
    """
    Retourner la liste des valeurs dupliquées(méthode optimisée)

    Args:
        numbers (list[int]): Liste d'entier à analyser

    Returns:
        list[int]: la liste de retour ou le resultat
    """
    seen: set[int] = set()
    duplicates: set[int] = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


def main(the_list: list[int]) -> None:

    # Calcul du temps optimal dans l'execution des fonctions

    # --- Mesure de la fonction non optimisée ---
    start = time.time()
    naive = find_duplicates_naive(the_list)
    end = time.time()
    time_naive = end - start

    # --- Mesure de la fontion optimisée ---
    start = time.time()
    optimized = find_duplicates_optimized(the_list)
    end = time.time()
    time_optimized = end - start

    print(f"Le resultat non optimisé est : {naive}")
    print(f"Le resultat optimisé est : {optimized}")
    print(f"Execution de la fonction non optimisée prend {time_naive:.6f} secondes")
    print(f"Execution de la fonction optimisée prend : {time_optimized:.6f} secondes")
    print(f"La fonction optimisée est {time_naive/time_optimized:.0f} x plus rapide")
    
liste_5000 = [random.randint(1, 100) for _ in range (5000)]
if __name__ == "__main__":
    main(liste_5000)

