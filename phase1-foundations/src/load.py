import sqlite3
from extract import extract_events
from transform import filter_valid_events, convert_types, add_event_date


def load_events(events: list[dict], db_path: str) -> int:
    """
    Insère les événements transformés dans la base SQLite.

    Args:
        events (list[dict]): Liste de dictionnaires d'événements tranformés.
        db_path (str): Chemin vers le fichier SQLite de destination.

    Returns:
        int: Nombre de lignes inseérés avec succès
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY,
                user_id TEXT NOT NULL,
                event_type TEXT NOT NULL,
                platform TEXT,
                country TEXT,
                timestamp TEXT,
                session_duration_sec INTEGER,
                event_date TEXT
            )
        """)

        cursor.executemany("""
            INSERT OR IGNORE INTO events VALUES
            (:event_id, :user_id, :event_type, :platform, :country, :timestamp, :session_duration_sec, :event_date)
        """, events)

        connection.commit()
        nbr_lignes = cursor.rowcount
    finally:
        connection.close()

    return nbr_lignes


def main() -> None:
    # Extract
    raw_data = extract_events("phase1-foundations/data/raw/events.csv")

    # Transform
    filtered = filter_valid_events(raw_data)
    typed = convert_types(filtered)
    transformed = add_event_date(typed)

    # Load
    n = load_events(transformed, "phase1-foundations/data/processed/appmetrics.db")
    print(f"{n} lignes insérées")
if __name__ == "__main__":
    main()
