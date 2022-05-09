#pip install pandas
#pip install requests

import requests
import pandas as pd

def API_connection():
    BASE_URL = 'https://reqres.in/'
    ENDPOINT = 'api/users?page=2/'
    resp = requests.get(BASE_URL + ENDPOINT)
    obj = resp.json()
    data = obj.get('data')
    df = pd.DataFrame(data)
    print(df)
    cname=df[df.first_name == 'Tobias']
    print(cname)

API_connection()