# data-warehouse-
# 🧾 Rapport Final — Mini Data Warehouse TP2

## Réalisé par : CAKPOSSE Eriyomi Phestèce Chancelle-Hélène


## 🎯 Objectif du projet

Ce TP vise à construire un mini Data Warehouse simulé, en suivant toutes les étapes d’un pipeline ETL : génération de données, nettoyage, modélisation en étoile, automatisation, visualisation et requêtage SQL.  
L’objectif est de comprendre les fondements d’un entrepôt de données et de manipuler des outils concrets comme pandas, DuckDB et matplotlib.


## 🏗️ Architecture du projet

Le projet est structuré en plusieurs dossiers :

- `data/raw` : données simulées (production, pannes)
- `data/staging` : données nettoyées et enrichies
- `data/dim` : dimensions (date, machine, produit)
- `data/fact` : faits (production, downtime)
- `src/etl` : scripts Python pour chaque étape
- `notebooks` : exploration, visualisation, requêtes SQL


## ⚙️ Pipeline ETL

### a. Génération des données (`generate_raw.py`)
- Simulation de 90 jours de production pour 3 machines et 3 produits
- Données de production et de pannes générées aléatoirement

### b. Nettoyage et enrichissement (`staging.py`)
- Calcul des unités bonnes, performance théorique, disponibilité
- Agrégation des pannes par jour et machine

### c. Modélisation en étoile (`build_dimensions.py`)
- Création des dimensions avec clés substitutives
- Enrichissement de la dimension date (année, mois, jour, jour de semaine)

### d. Construction des faits (`build_facts.py`)
- Jointures avec les dimensions
- Création des tables de faits prêtes pour l’analyse

### e. Orchestration (`run_all.py`)
- Exécution automatique de toutes les étapes du pipeline


## 📊 Visualisation des indicateurs

### a. OEE mensuel par machine (`visualisation.ipynb`)
- Calcul de l’OEE : disponibilité × performance × qualité
- Tracé de l’évolution mensuelle par machine

### b. Exploration des données (`traitements.ipynb`)
- Vérification des données à chaque étape
- Statistiques descriptives et contrôles qualité


## 🧠 Requêtes SQL analytiques

### a. Top produits les plus performants (`requetes_duckdb.ipynb`)
- Requête SQL pour identifier les produits avec la meilleure performance moyenne

### b. Requête OEE par machine et mois
- Agrégation SQL pour reproduire la visualisation en mode analytique

### c. Requête personnalisée (optionnelle)
- Possibilité d’ajouter des requêtes pour détecter les machines en sous-performance ou analyser les pannes


## 📌 Résultats et observations

- Les machines ont des performances variables selon les mois
- Le produit P1 est le plus performant dans cette simulation
- Le pipeline est entièrement automatisé et reproductible
- DuckDB permet des requêtes SQL rapides directement sur les fichiers CSV


## 🧪 Limites et extensions possibles

- Simulation simple : pas de saisonnalité ni de logique métier
- Possibilité d’ajouter des dimensions supplémentaires (opérateurs, lignes de production)
- Intégration future avec une base SQL ou un outil BI


## 👩‍💻 Conclusion

Ce projet m’a permis de consolider mes compétences en :

- Structuration de projet analytique
- Manipulation de données avec pandas
- Modélisation en étoile
- Automatisation avec Python
- Visualisation et requêtage SQL

Il constitue une base solide pour aborder des projets industriels plus complexes en Big Data et Intelligence Artificielle.



```python

```
