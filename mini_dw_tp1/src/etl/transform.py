import pandas as pd

def stage_customers(df):
    return df.assign(
        email=df["email"].str.strip().str.lower(),
        country=df["country"].str.upper()
    )

def stage_products(df):
    return df.assign(
        category=df["category"].str.title(),
        brand=df["brand"].str.title()
    )

def stage_orders(df):
    df["order_ts"] = pd.to_datetime(df["order_ts"])
    return df

def stage_inventory(df):
    df["inventory_date"] = pd.to_datetime(df["inventory_date"])
    return df
 
