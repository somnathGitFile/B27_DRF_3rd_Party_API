import requests
import pandas as pd

def API_connection():
    BASE_URL = 'https://data.covid19india.org/'
    ENDPOINT = 'v4/min/data.min.json'

    resp = requests.get(BASE_URL + ENDPOINT)
    obj = resp.json()
    data = obj.get('MH')
    data1 = data.get('districts')
    data2 = data1.get('Pune')

    df = pd.DataFrame(data2)
    print(df)
    Pune_V2 =df[df.index == 'vaccinated2']
    print(Pune_V2)

API_connection()