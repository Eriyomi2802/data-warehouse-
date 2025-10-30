import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/staging")

def save_df(df, name):
    path = DATA_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    print(f"✅ Saved: {path}")
 
