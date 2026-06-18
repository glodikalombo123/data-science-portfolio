# data_structures.py
# Exercice : comparer le temps d'exécution entre liste et dictionnaire

import time

# --- Partie 1 :  Construction des structures ---

size = 1_000_000

# Une liste d'entier de 0 à 999999
my_list = list(range(size))

# Un dictionnaire {entier : True} pour les mêmes valeurs
my_dict = {i: True for i in range(size)}


# --- Partie 2 : Recherche ---

target = 999_999 # Pire cas : l'élément est à la fin

# Recherche dans la liste
start = time.time()
result_list = target in my_list

end = time.time()
time_list = end - start

# Recherche dans le dictionnaire
start = time.time()
result_dict = target in my_dict
end = time.time()
time_dict = end - start


# --- Partie 3 : Affichage des resultats ---

print(f"Recherche dans la liste : {time_list:.6f} secondes | Trouvé : {result_list}")
print(f"Recherche dans le dico  : {time_dict:.6f} secondes | Trouvé : {result_dict}")
print(f"Le dictionnaire est {time_list / time_dict:.0f}x plus rapide")