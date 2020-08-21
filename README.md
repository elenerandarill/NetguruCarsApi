## README


# Name: Cars API


## Description
Application collecting data from `https://vpic.nhtsa.dot.gov/api/` and presenting results for chosen **car make** and **model name**. 
Every new response from that site(if the car exists) is being saved within database (cars make and model name). 
The car can be **rated** from **1** to **5**. 
User can check out the **list of all cars**, with their current average rate, requested so far.
User can also see **popular cars**, so a list starting with the biggest *number of rates* (not the average rate) given to the car.


## Installation & Requirements
```
Python 3+, Django 3+, Django Rest Framework 3+, requests 2.2+

pip install -r requirements.txt

```
Written on Windows 10


## Usage

-----------------------------------------------

To run application locally use this in commandline inside of `NetguruCarsApi/CarsApi-project`:

```
python manage.py runserver
```

To run tests locally use this in commandline inside of `NetguruCarsApi/CarsApi-project`:

```
python manage.py test
```

-----------------------------------------------


### Adding a new car

*Endpoint:* `/cars/`

- request method `POST`
Client must provide the *make* of the car and *model name* of the car.

**example**:
```
{"make": "tesla", "model_name": "model y"}
```

*Possible answers*: 
- `200` - ok - "Car of 'make' and 'model' exists!"
- `404` - not found - "Car of 'make' and 'model' does not exist. Please, double-check it."
- `404` - not found + error
- `405` - method not allowed

*If that (proper)car model is already present in database, saving it will be omitted.*

-----------------------------------------------

### Rating a car

*Endpoint:* `/rate/`

- request method `POST`
Client must provide the *make* of the car, *model name* of the car and rate from **1 to 5**.

**example**:
```
{"make": "tesla", "model_name": "model s", "rate": "5"}
```

*Possible answers*: 
- `201` - created - "Success! You have rated the car."
- `404` - not found - "This car is not in our database yet."
- `404` - not found + error
- `405` - method not allowed

*...Of course when it comes to rating Tesla the only legitimate rate is 5 ;))*

-----------------------------------------------

### List of all registered cars

*Endpoint:*	`/cars/`


- request method `GET`
List is ordered by the `make` of the car. Shows *make*, *model* and *average rate* of each car.

*Possible answer*:
```
HTTP `200` OK
[
    {
        "make": "honda",
        "model_name": "civic",
        "average_rate": 0.0
    },
    {
        "make": "tesla",
        "model_name": "model s",
        "average_rate": 4.7
    },
    {
        "make": "tesla",
        "model_name": "model 3",
        "average_rate": 5.0
    },
    ...
]
```

-----------------------------------------------

### Most popular cars

*Endpoint:* `/popular/`

- request method `GET`
List is ordered by the number of rates (`rates_counter`), from most to least popular.


*Possible answers*: 
```
HTTP `200` OK
[
    {
        "make": "tesla",
        "model_name": "model s",
        "rates_counter": 3,
        "average_rate": 4.7
    },
    {
        "make": "tesla",
        "model_name": "model y",
        "rates_counter": 2,
        "average_rate": 4.5
    },
    {
        "make": "tesla",
        "model_name": "model 3",
        "rates_counter": 1,
        "average_rate": 5.0
    },
	...
]
```

-----------------------------------------------


## Authors and acknowledgment
paulina.wojno@gmail.com


## Project status
Under develop.

