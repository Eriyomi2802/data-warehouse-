import pandas as pd
from pathlib import Path

# 📁 Dossiers
stg_dir = Path("data/staging")
dim_dir = Path("data/dim")
dim_dir.mkdir(parents=True, exist_ok=True)

# 📦 Chargement des données staging
df_prod = pd.read_csv(stg_dir / "stg_production.csv")

# 📅 Dimension date
df_date = pd.DataFrame({"date": pd.to_datetime(df_prod["date"].unique())})
df_date["date_sk"] = df_date.index + 1
df_date["year"] = df_date["date"].dt.year
df_date["month"] = df_date["date"].dt.month
df_date["day"] = df_date["date"].dt.day
df_date["weekday"] = df_date["date"].dt.day_name()
df_date.to_csv(dim_dir / "dim_date.csv", index=False)

# 🏭 Dimension machine
df_machine = pd.DataFrame({"machine_id": df_prod["machine_id"].unique()})
df_machine["machine_sk"] = df_machine.index + 1
df_machine.to_csv(dim_dir / "dim_machine.csv", index=False)

# 📦 Dimension produit
df_product = pd.DataFrame({"sku": df_prod["sku"].unique()})
df_product["product_sk"] = df_product.index + 1
df_product.to_csv(dim_dir / "dim_product.csv", index=False)

print("✅ Dimensions construites dans data/dim/")

