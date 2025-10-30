import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

def load_raw_data():
    return {
        "customers": pd.read_csv(DATA_DIR / "raw_customers.csv"),
        "products": pd.read_csv(DATA_DIR / "raw_products.csv"),
        "orders": pd.read_csv(DATA_DIR / "raw_orders.csv"),
        "promotions": pd.read_csv(DATA_DIR / "raw_promotions.csv"),
        "inventory": pd.read_csv(DATA_DIR / "raw_inventory.csv"),
    }
 
