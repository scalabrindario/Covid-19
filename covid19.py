import requests
import json
import pandas as pd

country = "italy"
start_date = "2020-03-01"
end_date = "2020-03-01"


def country_cases(country, start_date, end_date):
    # Creating the URL to make the API call
    URL = "https://api.covid19api.com/country/"+ country + "/status/confirmed?from=" + start_date + "T00:00:00Z&to=" + end_date +"T00:00:00Z"
    # Make the API call
    r = requests.get(URL)
    # Load the JSON, and convert into a text
    info = json.loads(r.text)
    # Convert JSON into a dataframe
    df = pd.json_normalize(info)
    
    return df


def live_cases_world(URL = "https://api.covid19api.com/summary"):
    # Make the API call
    r = requests.get(URL)
    # Load the JSON, and convert into a text
    info = json.loads(r.text)
    # Convert JSON into a dataframe
    df = pd.json_normalize(info, 'Countries')
    
    return df.set_index("Country")
