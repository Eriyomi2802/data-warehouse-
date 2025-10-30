import pandas as pd
from pathlib import Path

# 📁 Dossiers
stg_dir = Path("data/staging")
dim_dir = Path("data/dim")
fact_dir = Path("data/fact")
fact_dir.mkdir(parents=True, exist_ok=True)

# 📦 Chargement des données staging
df_prod = pd.read_csv(stg_dir / "stg_production.csv")
df_down = pd.read_csv(stg_dir / "stg_downtime.csv")

# 📦 Chargement des dimensions
dim_date = pd.read_csv(dim_dir / "dim_date.csv")
dim_machine = pd.read_csv(dim_dir / "dim_machine.csv")
dim_product = pd.read_csv(dim_dir / "dim_product.csv")

# 🔗 Jointures pour production
df_prod["date"] = pd.to_datetime(df_prod["date"])
dim_date["date"] = pd.to_datetime(dim_date["date"])
df_prod = df_prod.merge(dim_date[["date", "date_sk"]], on="date")
df_prod = df_prod.merge(dim_machine, on="machine_id")
df_prod = df_prod.merge(dim_product, on="sku")

# 💾 Table de faits production
fact_prod = df_prod[[
    "date_sk", "machine_sk", "product_sk",
    "units_total", "units_scrap", "units_good",
    "planned_minutes", "ideal_rate_per_min", "performance_units"
]]
fact_prod.to_csv(fact_dir / "fact_production.csv", index=False)

# 🔗 Jointures pour downtime
df_down["date"] = pd.to_datetime(df_down["date"])
df_down = df_down.merge(dim_date[["date", "date_sk"]], on="date")
df_down = df_down.merge(dim_machine, on="machine_id")

# 💾 Table de faits downtime
fact_down = df_down[["date_sk", "machine_sk", "minutes_down"]]
fact_down.to_csv(fact_dir / "fact_downtime.csv", index=False)

print("✅ Tables de faits construites dans data/fact/")

