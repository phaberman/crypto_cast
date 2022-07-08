import pandas as pd

path = 'data/btc.csv'

df = pd.read_csv(path)

print(df.open_rate.mean())
