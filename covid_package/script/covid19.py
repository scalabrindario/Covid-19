import requests
import json
import pandas as pd

def live_cases_world(URL = "https://api.covid19api.com/summary"):
    # Make the API call
    r = requests.get(URL)
    # Load the JSON, and convert into a text
    info = json.loads(r.text)
    # Convert JSON into a dataframe
    df = pd.json_normalize(info, 'Countries')
    
    return df.set_index("CountryCode")
