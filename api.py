import requests
import pandas as pd

BASE_URL = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=1DAY&'
headers = {'X-CoinAPI-Key' : 'E3431EAA-6678-4EEC-83FA-C2B57F4F0D81'}
time_start = "2021-01-01"
time_end = "2021-12-31"

def get_rates(time_start, time_end):
    # Join base url to input parameters
    url = BASE_URL + f"time_start={str(time_start)}&time_end={str(time_end)}&limit=366"
    # Call api
    response = requests.get(url, headers=headers).json()
    # Extract rates from response
    rates = []
    for i in response:
        rates.append(round(i['rate_open'], 2))
    # Extract dates from response (trimming off the timestamp)
    dates = []
    for i in response:
        dates.append(i['time_period_start'][0:10])
    # Create a dictionary from lists
    rates_dict = {'date': dates, 'open_rate': rates}
    # Turn dictionary into pandas dataframe
    return pd.DataFrame(rates_dict)

df = get_rates(time_start, time_end)

df.to_csv('data/btc.csv', index=False)
