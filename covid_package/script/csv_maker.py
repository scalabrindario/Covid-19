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

def country_check(path):
	try:
		# Storing information abount countries
		country_df = pd.read_csv(path, sep = ";")
		country_df = country_df.set_index("ISO2")
		return list(country_df.index)

	except FileNotFoundError:
	    print("The file does not exist")
	    return

	except ValueError:
		print("File has a wrong encoding")
		return

	except UnicodeDecodeError:
		print("File has a wrong encoding")
		return
	

def country_name(path, code):
	# Storing information abount countries
	country_df = pd.read_csv(path, sep = ";")
	country_df = country_df.set_index("ISO2")

	return country_df.loc[code]["Country"]

	

df = get_country_code()
df.to_csv("covid_package/csv/country_list.csv", sep = ";")