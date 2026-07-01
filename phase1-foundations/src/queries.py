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

    execute_and_display(
        cursor,
        "SELECT name, department, salary, AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary FROM employees",
        "Affichage du salaire de chaque employé et calcule de la moyenne du departement sans fusion des lignes"
    )

    execute_and_display(
        cursor,
        "SELECT name, department, salary, RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept FROM employees",
        "Classement des employés par salaire à l'intérieur des departements respetifs"
    )


    execute_and_display(
        cursor,
        "WITH department_averages AS (SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department) SELECT * FROM department_averages WHERE avg_salary > 70000",
        "Les departements dont le salaires moyens depassent 70000"
    )

    execute_and_display(
        cursor,
        "SELECT name, hire_year, salary, MAX(salary) OVER (PARTITION BY hire_year) AS max_salary_year FROM employees",
        "Les details des employés"
    )

    execute_and_display(
        cursor,
        "SELECT name, department, hire_year, RANK() OVER(ORDER BY hire_year) AS seniority_rank FROM employees",
        "Ranking des employés"
    )

    execute_and_display(
        cursor,
        """WITH dept_stats AS (
            SELECT
                e.department,
                COUNT(e.id) AS employee_count,
                d.budget,
                d.budget / COUNT(e.id) AS budget_per_employee
            FROM employees e
            INNER JOIN departments d ON e.department = d.name
            GROUP BY e.department
        )
        SELECT *
        FROM dept_stats
        WHERE budget_per_employee > 100000""",
        "Le nombre d'employé et le budget par employé depassant 100000 :"
    )

    conn.close()


if __name__ == "__main__":
    main()



