import sqlite3

def create_employees_table(db_path: str) -> None:
    """
    Crée une table 'employees' avec des données factices pour la pratique SQL.

    Args:
        db_path (str): Chemin vers le fichier de base de données SQLite.
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL,
            hire_year INTEGER NOT NULL
        )
    """)

    employees_data = [
        (1, "Alice Martin", "Engineering", 95000, 2021),
        (2, "Bob Dupont", "Engineering", 87000, 2022),
        (3, "Claire Bernard", "Marketing", 65000, 2020),
        (4, "David Lefevre", "Engineering", 102000, 2019),
        (5, "Emma Rousseau", "Sales", 58000, 2023),
        (6, "Felix Moreau", "Marketing", 71000, 2021),
        (7, "Gabrielle Petit", "Engineering", 110000, 2018),
        (8, "Hugo Lambert", "Sales", 62000, 2022)
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?)",
        employees_data
    )

    connection.commit()
    connection.close()
    print(f"Base de données créee avec succès : {db_path}")


def create_departments_table(db_path: str) -> None:
    """
    Créer une table departements avec des données factices.

    Args:
        db_path (str): Chemin vers le fichier de base de données SQLite.
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            budget INTEGER NOT NULL
        )
    """)

    departments_data = [
        (1, "Engineering", 500000),
        (2, "Marketing", 200000),
        (3, "Sales", 150000)
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO departments VALUES (?, ?, ?)",
        departments_data
    )

    connection.commit()
    connection.close()
    print(f"Table departements créée avec succès : {db_path}")

if __name__ == "__main__":
    db_path = "phase1-foundations/data/company.db"
    create_employees_table(db_path)
    create_departments_table(db_path)

