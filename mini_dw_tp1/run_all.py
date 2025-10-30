import os

print("▶️ Étape 1 : Exécution du pipeline ETL")
os.system("python main.py")

print("▶️ Étape 2 : Construction des tables de faits")
os.system("python src/etl/build_fact.py")

print("▶️ Étape 3 : Génération des visualisations")
os.system("jupyter nbconvert --to notebook --execute notebooks/visualisation.ipynb")

print("✅ Pipeline complet exécuté avec succès")
 
