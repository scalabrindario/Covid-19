import requests
import json
import pandas as pd

def get_country_code(URL = "https://api.covid19api.com/countries"):
    # Make the API call
    r = requests.get(URL)
    # Load the JSON, and convert into a text
    info = json.loads(r.text)
    # Convert JSON into a dataframe
    df = pd.json_normalize(info)
    
    return df

df = get_country_code()
df.to_csv("../csv/country_list.csv", sep = ";")