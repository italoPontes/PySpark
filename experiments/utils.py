import pandas as pd
import numpy as np

def get_dataset(size: int = 0) -> pd.DataFrame:
    df = pd.DataFrame()
    df["NFe"] = np.random.randint(10_000_000, 99_999_999, size)
    df["Estado"] = np.random.choice(["PB", "PE", "SP", "RJ"], size)
    dates = pd.date_range('2023-01-01', '2024-12-31')
    df["Date"] = np.random.choice(dates, size)
    df["Item"] = np.random.choice(["Coca-Cola", "Água", "Pepsi"], size)
    df["Price"] = np.random.uniform(1, 5, size)
    return df

def set_dtypes(df: pd.DataFrame = []) -> pd.DataFrame:
    df["NFe"] = df["NFe"].astype('int64')
    df["Estado"] = df["Estado"].astype('category')
    df["Item"] = df["Item"].astype('category')
    df["Price"] = df["Price"].astype('float32')
    return df