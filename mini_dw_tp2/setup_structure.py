from pathlib import Path

# 📁 Dossier racine = dossier courant
root = Path(".")

# 📂 Sous-dossiers à créer
folders = [
    "data/raw",
    "data/staging",
    "data/dim",
    "data/fact",
    "notebooks",
    "src/etl",
    "src/utils",
    "tests"
]

# 🛠️ Création des dossiers
for folder in folders:
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Dossier créé : {path}")

# 📄 Fichiers de base
(root / "run_all.py").write_text(
    "# Script d'orchestration du pipeline\nprint('▶️ Pipeline en cours...')\n",
    encoding="utf-8"
)

(root / "requirements.txt").write_text(
    "pandas\nnumpy\nmatplotlib\nseaborn\nduckdb\npytest\njupyter\n",
    encoding="utf-8"
)

(root / "README.md").write_text(
    "# Mini Data Warehouse TP2\n\nPipeline de fabrication avec simulation, ETL, OEE et extensions avancées.\n",
    encoding="utf-8"
)

