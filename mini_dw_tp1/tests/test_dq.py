import pandas as pd

def test_email_format():
    df = pd.read_csv("data/staging/stg_customers.csv")
    assert df["email"].str.contains("@").all()

def test_no_nulls():
    df = pd.read_csv("data/staging/stg_orders.csv")
    assert df.notnull().all().all()
 
