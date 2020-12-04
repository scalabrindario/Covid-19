#  Check Covid-19 cases :microbe:

In this repository you can find a file named ```main.py``` that triggers the Covid-19's API in order to gather data about pandemic development.

By running ```$python main.py <country_code> -u admin -p admin```, we will provide you with up to date information about Covid-19 cases of the selected country.

For example, executing ```$python main.py IT -u admin -p admin```, the output will be akin to this: 

```
Italy live update as of 2020-11-27:
 - New Confirmed Cases: 29001
 - New Deaths Cases: 822
 - New Recoveries: 24031
```

The user will be able to select any **country** in the world, passing the corresponding **country_code** and, additionally, the **timespan**.


## Arguments' Description :mag_right: 

### Country Code 
The complete list of country codes is contained in a _csv_ file located in ```covid_package/csv/```. <br>
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
- **-t**: displays the timespan chosen by the user. As said before there are two different choices (_partial_ and _total_);
- **-u**: the username. This parameter is REQUIRED;
- **-p**: the password. This parameter is REQUIRED.

## How to manage the database :file_cabinet:
In order to run ```main.py``` the user needs to provide **username** and the relative **password**. <br> We set a default user with the following credentials:
- *username*: **admin**; 
- *password*: **admin**.

#### How to add a new user
In order to add a new user to the database, you have to run the ```database.py``` file with the command ```-a```. <br> You should also specify the new password. 

Here an example: ```$python database.py -a andrea -p helloworld```.

#### How to show all users
In order to show all the users in the database, you have to run the ```database.py``` file with the command ```-d```. <br> You **must login as admin**.

Here an example: ```$python database.py -u admin -p admin -d```.

## Testing Functionality :wrench: 
We tested part of our code, the specific folder is here ```covid_package/test/```. 
Inside this folder we created a module called ```test_csv_maker.py```. <br>
If you want to make some tests please run the following code: ```$python -m unittest -v -b covid_package/test/csv_maker.py ``` the output will be similar to this  

```
test_empty_datafile (covid_package.test.test_csv_maker.TestCovid19) ... ok
test_invalid_datafile (covid_package.test.test_csv_maker.TestCovid19) ... ok
test_no_datafile (covid_package.test.test_csv_maker.TestCovid19) ... ok
test_valid_datafile (covid_package.test.test_csv_maker.TestCovid19) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.011s

OK
```

## Project Requirements :warning:  
The project requires different Python libraries to run, namely ```json```, ```requests```, ```pandas```, ```hashlib```, ```os```, ```random```, ```sqlite3```, ```unittest``` and ```argparse```. 

## References :blue_book:
This API is offered by [Covid API](https://covid19api.com/), and the source of all the data is [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19). <br>
The APIs are documented in a [API documentation page](https://documenter.getpostman.com/view/10808728/SzS8rjbc) and can be further expanded with optional premium features. 

## Authors :technologist:

- Ballistri Luca, Student ID: 872254
- Parisi Andrea, Student ID: 874633
- Querci Pietro, Student ID: 872401
- Scalabrin Dario, Student ID: 872700

## License :page_facing_up:
[MIT](https://choosealicense.com/licenses/mit/)