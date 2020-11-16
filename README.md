# Implementation of Covid-19 data

In this repository you can find a file named ```covid19.py``` that implements two different function.

```country_cases(country_list, start_date, end_date)``` function given a list of countries and the time span, return a dataframe with all the Covid information in that specific time frames for all countries passed. 


```live_cases_world()``` function return a dataframe with all the daily covid information in that for every country of the world. This function is used in the ```main.py``` file to obtain the daily updates of Italy.

If you run the program, executing the main file with: ```python main.py``` it will give you an output similar to:

```
$python main.py

Italy live update: 
 - New Confirmed Cases: 40902 
 - New Deaths Cases: 550 
 - New Recoveries: 11480 

```

The project requires ```json```, ```requests``` and ```pandas``` modules to run. This API is offered by [Covid API](https://covid19api.com/), and the source of all the data is [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19). The APIs are documented in a [API documentation page](https://documenter.getpostman.com/view/10808728/SzS8rjbc) and can be further expanded with optional premium features. You are free to (optionally) explore the APIs and expand the program with other functionalities.

