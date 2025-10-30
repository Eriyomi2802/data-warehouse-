import os
import sys

def run_step(description, command):
    print(f"\n▶️ {description}")
    if os.system(command) != 0:
        print(f"❌ Échec : {command}")
        sys.exit(1)

# 🔍 Analyse des arguments
args = sys.argv[1:]
run_tests = "--test" in args
run_sql = "--sql" in args

# 🛠️ Pipeline principal
run_step("Étape 1 : Génération des données RAW", "python src/etl/generate_raw.py")
run_step("Étape 2 : Nettoyage et staging", "python src/etl/staging.py")
run_step("Étape 3 : Construction des dimensions", "python src/etl/build_dimensions.py")
run_step("Étape 4 : Construction des tables de faits", "python src/etl/build_facts.py")
run_step("Étape 5 : Visualisation OEE", "jupyter nbconvert --to notebook --execute notebooks/visualisation.ipynb")

# ✅ Optionnel : tests
if run_tests:
    run_step("Tests unitaires", "pytest tests")

# ✅ Optionnel : requêtes SQL
if run_sql:
    run_step("Exploration SQL avec DuckDB", "jupyter nbconvert --to notebook --execute notebooks/requetes_duckdb.ipynb")

print("\n✅ Pipeline exécuté avec succès.")
