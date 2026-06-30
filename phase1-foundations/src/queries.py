import sqlite3

def execute_and_display(cursor: sqlite3.Cursor, query: str, title: str) -> None:
    """
    Execute une requête SQL et affiche les resultats avec un titre.

    Args:
        cursor (sqlite3.Cursor): Curseur SQLite actif
        query (str): Requête SQL à executer
        title (str): Titre affiché avant les resultats
    """
    cursor.execute(query)
    resultats = cursor.fetchall()
    print(title)
    for ligne in resultats:
        print(ligne)
    print()


def main() -> None:
    """Execute les 4 requêtes d'analyse sur la table employees."""
    conn = sqlite3.connect("phase1-foundations/data/company.db")
    cursor = conn.cursor()

    execute_and_display(
        cursor,
        "SELECT * FROM employees WHERE department = 'Engineering'",
        "Liste de tous les employés du departement Engineering :"
    )

    execute_and_display(
        cursor,
        "SELECT name, salary FROM employees ORDER BY salary DESC",
        "Liste des noms et salaires ordonnés par salaire"
    )

    execute_and_display(
        cursor,
        "SELECT * FROM employees ORDER BY salary DESC LIMIT 3",
        "Liste des 3 salariés les mieux payés :"
    )

    execute_and_display(
        cursor,
        "SELECT * FROM employees WHERE hire_year > 2020",
        "Liste des employés embauchés après 2020 :"
    )

    execute_and_display(
        cursor,
        "SELECT department, AVG(salary) FROM employees GROUP BY department",
        "Le salaire moyen par departement"
    )

    execute_and_display(
        cursor,
        "SELECT department, COUNT(id) FROM employees GROUP BY department",
        "Liste d'employés par departement"
    )

    execute_and_display(
        cursor,
        "SELECT employees.name, departments.budget FROM employees INNER JOIN departments ON employees.department = departments.name;",
        "Le nom de chaque employé avec le budget de son departement"
    )

    conn.close()


if __name__ == "__main__":
    main()
