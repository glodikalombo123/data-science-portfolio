import sqlite3

def execute_and_display(cursor: sqlite3.Cursor, query: str, title: str) -> None:
    """
    Execute une reqête SQL et affiche les resultats avec un titre

    Args:
        cursor (sqlite3.Cursor): Curseur SQLite actif
        query (str): Reqête SQL à executer
        title (str): Titre affiché avant les resultats
    """
    cursor.execute(query)
    resultats = cursor.fetchall()
    print(title)
    for ligne in resultats:
        print(ligne)
    print()

def main() -> None:
    """ Execution des reqêtes d'analyse sur la table 'events' de appmetris.db """
    conn = sqlite3.connect("phase1-foundations/data/processed/appmetrics.db")
    cursor = conn.cursor()

    # --- PREMIERE REQUETE ---
    execute_and_display(
        cursor,
        """SELECT
            event_type,
            COUNT(event_id)
            FROM events
            GROUP BY event_type
            ORDER BY COUNT(event_id) DESC""",
        "Volume par type d'événement"
    )

    # --- DEUXIEME REQUETE ---
    execute_and_display(
        cursor,
        """SELECT
            event_date,
            COUNT(DISTINCT user_id)
            FROM events
            GROUP BY event_date""",
            "Utilisateurs actifs par jour"
    )

    # --- TROISIEME REQUETE ---
    execute_and_display(
        cursor,
        """SELECT
            platform,
            AVG (session_duration_sec)
        FROM events
        WHERE event_type NOT IN ('login')
        GROUP BY platform""",
        "Durée moyenne des session par plateforme"
    )

    # --- QUATRIEME REQUETE ---
    execute_and_display(
        cursor,
        """SELECT
            country,
            COUNT(event_id) AS total_events,
            SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS total_purchases
        FROM events
        GROUP BY country""",
        "Taux de conversion par pays"
    )

    # --- CINQUIEME REQUETE ---
    execute_and_display(
        cursor,
        """WITH user_totals AS(
            SELECT
                user_id,
                SUM(session_duration_sec) AS total_duration
            FROM events
            GROUP BY user_id
        )
        SELECT
            user_id,
            total_duration,
            RANK() OVER(ORDER BY total_duration DESC) AS rank
        FROM user_totals""",
        "Classement des utilisateurs par durée de session"
    )

    conn.close() 


if __name__ == "__main__":
    main()
