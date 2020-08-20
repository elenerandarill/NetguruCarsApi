## README


# Name: Cars API


## Description
Application collecting data from `https://vpic.nhtsa.dot.gov/api/` and presenting results for chosen **car make** and **model name**. 
Every new response from that site(if the car exists) is being saved within database (cars make and model name). 
The car can be `rated` from **1** to **5**. 
User can check out the **list of all cars**, with their current average rate, requested so far.
User can also see **5 Top Cars** which have the biggest *number of rates* (not the average rate).


## Installation & Requirements
```
Python 3+, Django 3+, Django Rest Framework 3+, requests 2.2+
```
Written on Windows 10


## Usage
-----------------------------------------------

### Finding/Adding a new Car

*Endpoint:*
https://localhost:8000/cars/find/

- request method `POST`
Client must provide the *make* of the car and *model name* of the car.

**example**:
```
{"make": "tesla", "model_name": "model y"}
```

*Possible answers*: 
- `200` - ok - "Car of 'make' make and 'model' exists!"
- `404` - not found - "Car of 'make' and 'model' does not exist. Please, double-check it."
- `404` - not found + error
- `405` - method not allowed

*If that (proper)car model is already present in database, saving it will be omitted.*
-----------------------------------------------

### Rating a car

*Endpoint:*
https://localhost:8000/cars/rate/

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

*...Of course if it comes to rating Tesla the only legitimate rate is 5 ;))*
-----------------------------------------------

### List of all registered Cars

*Endpoint:*
https://*****

- request method `GET`
...

*Possible answers*: 


-----------------------------------------------

### Top 5 most rated Cars

*Endpoint:*
https://*****

- request method `GET`
...

*Possible answers*: 



-----------------------------------------------


## Authors and acknowledgment
paulina.wojno@gmail.com


## Project status
Under develop.

