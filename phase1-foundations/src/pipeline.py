from extract import extract_events
from transform import filter_valid_events, convert_types, add_event_date
from load import load_events
from analyze import run_analysis


def run_pipeline():
    # Affiche message de début
    print("=== Démarrage du pipeline Appmetrics ===")

    # Extract
    raw_data = extract_events("phase1-foundations/data/raw/events.csv")

    # Transform
    filtered = filter_valid_events(raw_data)
    typed = convert_types(filtered)
    transformed = add_event_date(typed)

    # Load
    n = load_events(transformed, "phase1-foundations/data/processed/appmetrics.db")
    if n == 0:
        print("0 nouvelles lignes insérées (données déjà présentes en base)")
    else:
        print(f"{n} lignes insérées")

    # Analyse
    run_analysis()

    # Affichage message de fin
    print("=== Pipeline terminé avec succès ===")



if __name__ == "__main__":
    run_pipeline()

