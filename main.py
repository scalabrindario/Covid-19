from covid_package.script.covid19 import live_cases_world
from database import open_and_create, check_for_username
import argparse
import pandas as pd

# Pay attention not to modify the path
default_csv_path = "covid_package/csv/"
default_db_path = "covid_package/database/"

# Storing information abount countries
country_df = pd.read_csv(default_csv_path + "country_list.csv", sep = ";")
country_df = country_df.set_index("ISO2")

def parse_argument():
	parser = argparse.ArgumentParser()
	# Selection of the country through its country code that can be found in covid_package/csv/country_list.csv
	parser.add_argument("country_code", help = "The country code associated with each country", choices = list(country_df.index))
	# Selectio of the level of verbosity
	parser.add_argument("-v", help = "Be more verbose", action = "store_true")
	# Selection of the timespan for the data shown
	parser.add_argument("-t", default = "partial", help = "Timeframe of the cases", required = False, choices = ["partial", "total"])
	# Check username 
	parser.add_argument("-u", help = "Add a username (requires -p)", required = True)
	# Check password
	parser.add_argument("-p", help = "Insert the password", required = True) 

	return parser.parse_args()

country = parse_argument()

if __name__ == "__main__":
	# Open database and if necessary create the user table
	open_and_create(default_db_path + "database.db")

	if check_for_username(country.u, country.p):
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
			print("{} total cases since the breakout as of {}: \n - Total Confirmed Cases: {} \n - Total Deaths Cases: {} \n - Total Recoveries: {} ".format(country_name, date, total_cases, total_deaths, total_recovery)) 

	else:
		print ('Username does not exist or password is incorrect')