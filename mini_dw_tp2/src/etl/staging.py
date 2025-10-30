import pandas as pd
from pathlib import Path

# 📁 Dossiers
raw_dir = Path("data/raw")
stg_dir = Path("data/staging")
stg_dir.mkdir(parents=True, exist_ok=True)

# 📦 Chargement des données RAW
df_prod = pd.read_csv(raw_dir / "raw_production.csv")
df_down = pd.read_csv(raw_dir / "raw_downtime.csv")

# 🧹 Nettoyage production
df_prod["units_good"] = df_prod["units_total"] - df_prod["units_scrap"]
df_prod["availability_minutes"] = df_prod["planned_minutes"]  # sera ajusté plus tard avec les pannes
df_prod["performance_units"] = df_prod["ideal_rate_per_min"] * df_prod["planned_minutes"]
df_prod["date"] = pd.to_datetime(df_prod["date"])

# 💾 Sauvegarde staging production
df_prod.to_csv(stg_dir / "stg_production.csv", index=False)

# 🧹 Nettoyage downtime
df_down["date"] = pd.to_datetime(df_down["date"])
df_down = df_down.groupby(["date", "machine_id"], as_index=False)["minutes_down"].sum()

# 💾 Sauvegarde staging downtime
df_down.to_csv(stg_dir / "stg_downtime.csv", index=False)

print("✅ Données staging nettoyées et enrichies")
