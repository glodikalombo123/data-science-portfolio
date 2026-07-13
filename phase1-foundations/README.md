# AppMetrics ETL Pipeline

## Project Overview
End-to-end ETL pipeline built in Python and SQL to process mobile app event data.
Extracts raw CSV data, cleans and transforms it, loads it into SQLite,
and produces business metrics used in product analytics.

## Tech Stack
- Python 3.13(csv, sqlite3)
- SQLite
- Git / GitHub

## Pipeline Architecture
```
events.csv -> extract.py -> transform.py -> load.py -> appmetrics.db -> analyse.py
  (raw)         (read)          (clean)     (insert)    (database)      (insights)
```

## File Structure
```
phase1-foundations/
├── data/
│   ├── raw/events.csv          # Raw event data (20 records)
│   └── processed/              # SQLite database (generated)
└── src/
    ├── extract.py              # CSV reading and validation
    ├── transform.py            # Filtering, type conversion, enrichment
    ├── load.py                 # SQLite insertion
    ├── analyze.py              # SQL business metrics queries
    └── pipeline.py             # Main orchestrator
```
## How to Run
``` bash
git clone https://github.com/glodikalombo123/data-science-portfolio.git
cd data-science-portfolio
python phase1-foundations/src/pipeline.py
```

##  Business Insights Generated

1. Request 1 — Volume per type of event
login: 8 | view_product: 6 | purchase: 5
On 19 validated events, 5 are purchases — The Global rate conversion of 26% (5/19).

2. Request 2 — Daily active users
2024-01-15: 5 Users | 2024-01-16: 6 Users
DAU (Daily Active Users). We have a growth of +20% in one day (5→6).

3. Request 3 — Average time session by platform
Android: 260s | Web: 265s | iOS: 239s
Les durées sont proches The are not great difference of timing by platform (239-265 secondes, soit ~4 minutes), The user experience is almost the same between platform but IOS is quite down.
purchas
4. Request 4 — conversion rate by country

France:  7 events, 2 purchases → 28.6%
Sénégal: 4 events, 1 purchase  → 25%
Canada:  3 events, 1 purchase  → 33%
RDC:     3 events, 1 purchase  → 33%
Maroc:   2 events, 0 purchase  → 0%

Maroc = 0 purchase despite 2 visites. Canada and RDC have best rate conversion (33%)

5. Request 5 — User Ranking by time session
U003: 647s (rank 1) | U002: 532s | U004: 525s | U005: 510s | U001: 434s | U006: 150s

U003 is the most engaged user ( almost 11 minutes  of session cumulated). U006, has a very weak time session (150s)

## Skills Demonstrated

- Python — modular ETL pipeline with csv and sqlite3 standard libraries
- SQL — SELECT, WHERE, GROUP BY, JOIN, window functions (RANK, SUM OVER), CTEs
- Data Engineering — Extract / Transform / Load pipeline with idempotent insertion
- Algorithmic thinking — O(1) vs O(n) complexity, hash tables, set-based deduplication
- Business Analytics — DAU, conversion rate, session duration, user engagement ranking
- Git / GitHub : atomic commits, conventional commit messages, professional repo structure

Mais pour la partie  Business Insights Generated j'aimerai que toi tu me donne une réponse, ou soit que tu mette ma repose de manière plus adapté pour que ça ne soit pas amateur