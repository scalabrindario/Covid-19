from covid_package.script.covid19 import live_cases_world
import argparse
import pandas as pd

# Pay attention not to modify the path
default_csv_path = "covid_package/csv/"

# Storing information abount countries
country_df = pd.read_csv(default_csv_path + "country_list.csv", sep = ";")
country_df = country_df.set_index("ISO2")

parser = argparse.ArgumentParser()
parser.add_argument("-v", help = "Be more verbose", action = "store_true")
parser.add_argument("country_code", help = "The country code associated with each country", choices = list(country_df.index))
country = parser.parse_args()

df = live_cases_world()
new_cases = df.loc[country.country_code]["NewConfirmed"]
new_deaths = df.loc[country.country_code]["NewDeaths"]
new_recovery = df.loc[country.country_code]["NewRecovered"]

print("{} live update: \n - New Confirmed Cases: {} \n - New Deaths Cases: {} \n - New Recoveries: {} ".format(country_df.loc[country.country_code]["Country"], new_cases, new_deaths, new_recovery ))
