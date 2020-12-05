import requests
import json
import pandas as pd


def live_cases_world(URL="https://api.covid19api.com/summary"):
    """Creates a pandas dataframe with daily countries cases
       fetched through an API call and sets the index as the country code

       Keyword arguments:
       URL -- The url of the API call.
              The default URL is https://api.covid19api.com/summary
    """

    # Make the API call
    r = requests.get(URL)
    # Load the JSON, and convert into a text
    info = json.loads(r.text)
    # Convert JSON into a dataframe
    df = pd.json_normalize(info, 'Countries')
    return df.set_index("CountryCode")
