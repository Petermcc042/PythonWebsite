import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def get_columns(file_path):
    df = load_data(file_path)
    return list(df.columns)