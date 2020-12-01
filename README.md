#  Check Covid-19 cases :microbe:

In this repository you can find a file named ```main.py``` that triggers the Covid-19's API in order to gather data about pandemic development.

By running ```$python main.py <country_code>```, we will provide you with up to date information about Covid-19 cases of the selected country.

For example, executing ```$python main.py IT```, the output will be akin to this: 

```
Italy live update as of 2020-11-27:
 - New Confirmed Cases: 29001
 - New Deaths Cases: 822
 - New Recoveries: 24031
```

The user will be able to select any **country** in the world, passing the corresponding **country_code** and, additionally, the **timespan**.


## Arguments' Description :mag_right: 

### Country Code 
The complete list of country codes is contained in a _csv_ file located in ```covid_package/csv/```.
Some examples of country codes and corresponding country are:
 
| Country Code | Country Name|
|--------------|-------------|
|	 IT        |   Italy     | 
|	 FR        |   France    |
|	 GR        |   Germany   |
|	 ES        |   Spain     |
|	 AU        |   Australia |


### Timespan
The user can choose between two different timespans:

- **partial**: daily cases as of the most recent update, this is the _default_ option;
- **total**: overall cases since the breakout of the pandemic.


### Command line parameters :computer:
In order to execute the ```main.py``` file, some command line parameters must be passed to the shell.

#### Positional Argument 
- **country_code**: a unique code to identify a specific country (only one country code can be passed at a time)

#### Optional Argument
- **-h, --help**: displays all the possible options for each parameter; 
- **-v**:  displays the output with different levels of verbosity (at the moment only one level of verbosity is supported);
- **-t**: displays the timespan chosen by the user. As said before there are two different choices (_partial_ and _total_).


## Project Requirements :warning:  
The project requires different Python libraries to run, namely ```json```, ```requests```, ```pandas``` and ```argparse```. 

## References :blue_book:
This API is offered by [Covid API](https://covid19api.com/), and the source of all the data is [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19). The APIs are documented in a [API documentation page](https://documenter.getpostman.com/view/10808728/SzS8rjbc) and can be further expanded with optional premium features. 

## Authors :technologist:

- Ballistri Luca, Student ID: 872254
- Parisi Andrea, Student ID: 874633
- Querci Pietro, Student ID: 872401
- Scalabrin Dario, Student ID: 872700

## License :page_facing_up:
[MIT](https://choosealicense.com/licenses/mit/)