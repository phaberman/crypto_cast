# Import packages
import pandas as pd

# Function to load the csv as a dataframe
def import_data():
    path = 'data/btc.csv'
    return pd.read_csv(path)

# Function to rename the data columns
def rename_columns(df):
    df.columns = ['ds', 'y']
    return df

# Function to set datatype of columns
def set_dtypes(df):
    df['ds'] = pd.to_datetime(df['ds'])
    return df

# Function that combines previous functions into a pipline
def pipeline():
    df = import_data()
    df = rename_columns(df)
    df = set_dtypes(df)
    return df.to_csv('data/btc_clean.csv', index=False)

pipeline()
