from src.etl.extract import load_raw_data
from src.etl.transform import (
    stage_customers,
    stage_products,
    stage_orders,
    stage_inventory
)
from src.etl.load import save_df

def run_etl():
    raw = load_raw_data()

    stg_customers = stage_customers(raw["customers"])
    stg_products = stage_products(raw["products"])
    stg_orders = stage_orders(raw["orders"])
    stg_inventory = stage_inventory(raw["inventory"])

    save_df(stg_customers, "stg_customers")
    save_df(stg_products, "stg_products")
    save_df(stg_orders, "stg_orders")
    save_df(stg_inventory, "stg_inventory")

if __name__ == "__main__":
    run_etl()
 
