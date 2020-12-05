
from covid_package.script.covid19 import live_cases_world
from database import open_and_create, check_for_username
from covid_package.script.csv_maker import country_check, country_name
import argparse
import pandas as pd

# Pay attention not to modify the path
default_csv_path = "covid_package/csv/"
default_db_path = "covid_package/database/"


def parse_argument():
    """Parse the arguments in order to access multiple functionalities
    """
    parser = argparse.ArgumentParser()
    # Selection of the country through its country code
    parser.add_argument("country_code",
                        help="The country code associated with each country")
    # Selectio of the level of verbosity
    parser.add_argument("-v", help="Be more verbose", action="store_true")
    # Selection of the timespan for the data shown
    parser.add_argument("-t", default="partial",
                        help="Timeframe of the cases",
                        required=False, choices=["partial", "total"])
    # Check username
    parser.add_argument(
        "-u", help="Add a username (requires -p)", required=True)
    # Check password
    parser.add_argument("-p", help="Insert the password", required=True)

    return parser.parse_args()


country = parse_argument()

if country.country_code in country_check(
                            default_csv_path + "country_list.csv"):
    if __name__ == "__main__":
        # Open database and if necessary create the user table
        open_and_create(default_db_path + "database.db")

        if check_for_username(country.u, country.p):
            df = live_cases_world()
            # Name of the selected country code
            country_name = country_name(
                default_csv_path + "country_list.csv", country.country_code)
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
                print("{} live update as of {}:".format(country_name, date))
                print("- New Confirmed Cases: {}".format(new_cases))
                print("- New Deaths Cases: {}".format(new_deaths))
                print("- New Recoveries: {}".format(new_recovery))

            elif country.t == "total":
                print("{} total cases since {}:".format(country_name, date))
                print("- Total Confirmed Cases: {}".format(total_cases))
                print("- Total Deaths Cases: {}".format(total_deaths))
                print("- Total Recoveries Cases: {}".format(total_recovery))

        else:
            print('Username does not exist or password is incorrect')
else:
    print('Please type a correct country code')
