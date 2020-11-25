import requests
import json
import pandas as pd

def country_cases(country_list, start_date, end_date):

    # Create new dataset
    aggregate_df = pd.DataFrame()

    for country in country_list:
        # Creating the URL to make the API call
        URL = "https://api.covid19api.com/country/"+ country + "/status/confirmed?from=" + start_date + "T00:00:00Z&to=" + end_date +"T00:00:00Z"
        # Make the API call
        r = requests.get(URL)
        # Load the JSON, and convert into a text
        info = json.loads(r.text)
        # Convert JSON into a dataframe
        df = pd.json_normalize(info)
        # Sum values for the same province
        df = df.groupby(['Country','Date'])['Cases'].sum().reset_index()
        # Append dataframe to the general one
        aggregate_df = aggregate_df.append(df)
        
    # Convert Date column in datetime format
    aggregate_df['Date'] = pd.to_datetime(aggregate_df.Date).dt.strftime('%Y/%m/%d')
    
    # Pivot the dataframe
    aggregate_df = aggregate_df.pivot(index = 'Country', columns = 'Date')['Cases']
    
    return aggregate_df


def live_cases_world(URL = "https://api.covid19api.com/summary"):
    # Make the API call
    r = requests.get(URL)
    # Load the JSON, and convert into a text
    info = json.loads(r.text)
    # Convert JSON into a dataframe
    df = pd.json_normalize(info, 'Countries')
    
    return df.set_index("CountryCode")
