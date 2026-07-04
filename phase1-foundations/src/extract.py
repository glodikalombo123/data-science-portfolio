import csv

def extract_events(filepath : str) -> list[dict]:
    """
    Lit le fichier CSV des événements et retourne une liste de dictionnaires.

    Args:
        filepath (str): Chemin vers le fichier CSV brut.

    Returns:
        list[dict]: Liste des dictionnaires, une entrée par ligne du CSV.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """

    try:
        with open(filepath, encoding= "utf-8") as f :
            data = [row for row in csv.DictReader(f)]
        return data
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable -> {filepath}")
        return []

def main(the_path : str) -> None:

    list_dictionnaire = extract_events(the_path)

    line_nbr = len(list_dictionnaire)
    print(f"Le fihier contient {line_nbr} lignes")
    print(f"Les 3 premiers éléments de la liste sont ----- : {list_dictionnaire[0:3]}")

if __name__ == "__main__":
    main("phase1-foundations/data/raw/events.csv")