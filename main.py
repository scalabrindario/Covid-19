from covid_package.covid19 import live_cases_world
import pandas as pd 

df = live_cases_world()

country = "Italy"

new_cases = df.loc[country]["NewConfirmed"]
new_deaths = df.loc[country]["NewDeaths"]
new_recovery = df.loc[country]["NewRecovered"]

print("{} live update: \n - New Confirmed Cases: {} \n - New Deaths Cases: {} \n - New Recoveries: {} ".format(country, new_cases, new_deaths, new_recovery ))
