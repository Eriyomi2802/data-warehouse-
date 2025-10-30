import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data/staging")
OUT_DIR = Path("data")
OUT_DIR.mkdir(exist_ok=True)

# Load staging data
customers = pd.read_csv(DATA_DIR / "stg_customers.csv")
products = pd.read_csv(DATA_DIR / "stg_products.csv")
orders = pd.read_csv(DATA_DIR / "stg_orders.csv")
inventory = pd.read_csv(DATA_DIR / "stg_inventory.csv")
promotions = pd.read_csv(DATA_DIR / "stg_promotions.csv") if (DATA_DIR / "stg_promotions.csv").exists() else None

# DIMENSIONS
def build_dim_customer():
    dim = customers.drop_duplicates("customer_id").reset_index(drop=True)
    dim["customer_sk"] = range(1, len(dim)+1)
    dim.to_csv(OUT_DIR / "dim/dim_customer.csv", index=False)
    return dim

def build_dim_product():
    dim = products.drop_duplicates("product_id").reset_index(drop=True)
    dim["product_sk"] = range(1, len(dim)+1)
    dim.to_csv(OUT_DIR / "dim/dim_product.csv", index=False)
    return dim

def build_dim_date():
    dates = pd.to_datetime(orders["order_ts"]).dt.normalize().unique()
    dim = pd.DataFrame({"date": pd.to_datetime(sorted(dates))})
    dim["date_sk"] = range(1, len(dim)+1)
    dim["day"] = dim["date"].dt.day
    dim["month"] = dim["date"].dt.month
    dim["quarter"] = dim["date"].dt.quarter
    dim["year"] = dim["date"].dt.year
    dim.to_csv(OUT_DIR / "dim/dim_date.csv", index=False)
    return dim

def build_dim_promotion():
    if promotions is not None:
        dim = promotions.drop_duplicates("promotion_id").reset_index(drop=True)
        dim["promotion_sk"] = range(1, len(dim)+1)
        dim.to_csv(OUT_DIR / "dim/dim_promotion.csv", index=False)
        return dim
    return None

# FACT SALES
def build_fact_sales(dim_customer, dim_product, dim_date, dim_promotion=None):
    fact = orders.copy()
    fact["order_ts"] = pd.to_datetime(fact["order_ts"])
    fact = fact.merge(dim_customer[["customer_id", "customer_sk"]], on="customer_id")
    fact = fact.merge(dim_product[["product_id", "product_sk", "unit_price", "unit_cost"]], on="product_id")
    fact = fact.merge(dim_date[["date", "date_sk"]], left_on=fact["order_ts"].dt.normalize(), right_on="date")

    fact["amount"] = fact["quantity"] * fact["unit_price"]
    fact["cost"] = fact["quantity"] * fact["unit_cost"]
    fact["margin"] = fact["amount"] - fact["cost"]

    if dim_promotion is not None:
        rng = pd.Series(pd.Series(range(len(fact))).sample(frac=1).values)
        fact["promotion_id"] = rng % len(dim_promotion) + 1
        fact = fact.merge(dim_promotion[["promotion_id", "promotion_sk"]], on="promotion_id", how="left")

    fact_sales = fact[["order_id", "order_line_id", "date_sk", "product_sk", "customer_sk", "quantity", "unit_price", "amount", "cost", "margin"]]
    if dim_promotion is not None:
        fact_sales["promotion_sk"] = fact["promotion_sk"]

    fact_sales.to_csv(OUT_DIR / "fact/fact_sales.csv", index=False)
    return fact_sales

# FACT INVENTORY
def build_fact_inventory(dim_product, dim_date):
    inventory["inventory_date"] = pd.to_datetime(inventory["inventory_date"])
    fact = inventory.merge(dim_product[["product_id", "product_sk"]], on="product_id")
    fact = fact.merge(dim_date[["date", "date_sk"]], left_on="inventory_date", right_on="date")
    fact_inventory = fact[["date_sk", "product_sk", "stock_qty"]]
    fact_inventory.to_csv(OUT_DIR / "fact/fact_inventory.csv", index=False)

# AGGREGATIONS
def build_aggregates(fact_sales, dim_date, dim_product):
    sales_by_month = fact_sales.merge(dim_date[["date_sk", "month", "year"]], on="date_sk")
    sales_by_month = sales_by_month.groupby(["year", "month"], as_index=False)["amount"].sum()
    sales_by_month.to_csv(OUT_DIR / "sales_by_month.csv", index=False)

    top_products = fact_sales.merge(dim_product[["product_sk", "product_name"]], on="product_sk")
    top_products = top_products.groupby(["product_sk", "product_name"], as_index=False)["amount"].sum()
    top_products = top_products.sort_values("amount", ascending=False).head(10)
    top_products.to_csv(OUT_DIR / "top_10_products.csv", index=False)

    weekly_sales = fact_sales.merge(dim_date[["date_sk", "date"]], on="date_sk")
    weekly_sales["week"] = weekly_sales["date"].dt.isocalendar().week
    weekly_sales["year"] = weekly_sales["date"].dt.year
    weekly_sales = weekly_sales.groupby(["year", "week"], as_index=False)["amount"].sum()
    weekly_sales.to_csv(OUT_DIR / "weekly_sales_view.csv", index=False)

# RUN ALL
def run():
    dim_customer = build_dim_customer()
    dim_product = build_dim_product()
    dim_date = build_dim_date()
    dim_promotion = build_dim_promotion()
    fact_sales = build_fact_sales(dim_customer, dim_product, dim_date, dim_promotion)
    build_fact_inventory(dim_product, dim_date)
    build_aggregates(fact_sales, dim_date, dim_product)

if __name__ == "__main__":
    run()
