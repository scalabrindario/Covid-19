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
# Selection of the timespan for the data shown
parser.add_argument("-t", default = "partial", help = "Timeframe of the cases", required = False, choices = ["partial", "total"])
# Selection of the country through its country code that can be found in covid_package/csv/country_list.csv
parser.add_argument("country_code", help = "The country code associated with each country", choices = list(country_df.index))
country = parser.parse_args()

df = live_cases_world()

# Name of the selected country code
country_name = country_df.loc[country.country_code]["Country"]
# Date of the last update
date = df.loc[country.country_code]["Date"][:10]
# Most recent confirmed cases
new_cases = df.loc[country.country_code]["NewConfirmed"]
# Most recent confirmed deaths
new_deaths = df.loc[country.country_code]["NewDeaths"]
# Most recent confirmed recoveries
new_recovery = df.loc[country.country_code]["NewRecovered"]
# Overall confirmed cases
total_cases = df.loc[country.country_code]["TotalConfirmed"]
# Overall confirmed deaths
total_deaths = df.loc[country.country_code]["TotalDeaths"]
# Overall confirmed recoveries
total_recovery = df.loc[country.country_code]["TotalRecovered"]

# Definition of the behaviour based on timespan selection
if country.t == "partial": 
	print("{} live update as of {}: \n - New Confirmed Cases: {} \n - New Deaths Cases: {} \n - New Recoveries: {} ".format(country_name, date, new_cases, new_deaths, new_recovery ))
elif country.t == "total":
	print("{} total cases since the breakout as of {}: \n - Total Confirmed Cases: {} \n - Total Deaths Cases: {} \n - Total Recoveries: {} ".format(country_name, date, total_cases, total_deaths, total_recovery ))