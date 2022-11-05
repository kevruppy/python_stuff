import numpy as np
import pandas as pd
from functools import wraps

df=pd.DataFrame({"date":["2022-10-29", "2022-09-30", "2022-10-10"], "price":["27.95", "33.23", "22.45"], "sales_qty":[261, 311, 289]})

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"The size after {func.__name__} is {result.shape}.")
        return result
    return wrapper

@logging
def start_pipeline(df):
    return df.copy()
@logging
def handle_dtypes(df):
    df["date"] = df["date"].astype("datetime64[ns]")
    return df
@logging
def fill_missing_prices(df):
    df["price"].fillna(method="ffill", inplace=True)
    return df
@logging
def remove_outliers(df, threshold=2000):
    return df[df["sales_qty"] <= threshold].reset_index(drop=True)
    
df_processed = (df.
                 pipe(start_pipeline).
                 pipe(handle_dtypes).
                 pipe(fill_missing_prices).
                 pipe(remove_outliers, threshold=1500))