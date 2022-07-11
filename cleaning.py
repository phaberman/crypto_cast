# Import packages
import pandas as pd

# Import data
def import_data():
    path = 'data/btc.csv'
    return pd.read_csv(path)

# Change column names
def change_col_names(df):
    df.columns = ['ds', 'y']
    return df 

# Export to csv
def export_csv(df):
    return df.to_csv('data/btc_clean.csv', index=False)

# Pipeline
def pipeline():
    df = import_data()
    df = change_col_names(df)
    return export_csv(df)

pipeline()
