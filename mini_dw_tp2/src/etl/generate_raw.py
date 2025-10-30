import pandas as pd
import numpy as np
from pathlib import Path

# 📁 Dossier de sortie
raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

# 📅 Simulation de 90 jours
dates = pd.date_range("2023-01-01", periods=90, freq="D")
machines = ["M1", "M2", "M3"]
products = ["P1", "P2", "P3"]

# 🏭 Données de production
df_prod = pd.DataFrame({
    "date": dates,
    "machine_id": np.random.choice(machines, size=90),
    "sku": np.random.choice(products, size=90),
    "units_total": np.random.randint(100, 300, size=90),
    "units_scrap": np.random.randint(0, 30, size=90),
    "planned_minutes": 480,
    "ideal_rate_per_min": np.random.uniform(0.5, 1.2, size=90).round(2)
})
df_prod.to_csv(raw_dir / "raw_production.csv", index=False)

# ⚠️ Données de pannes
df_down = pd.DataFrame({
    "date": dates,
    "machine_id": np.random.choice(machines, size=90),
    "minutes_down": np.random.randint(0, 60, size=90)
})
df_down.to_csv(raw_dir / "raw_downtime.csv", index=False)

print("✅ Données RAW générées dans data/raw/")
