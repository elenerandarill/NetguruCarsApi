## README


# Name: Cars API


## Description
Application collecting data from `https://vpic.nhtsa.dot.gov/api/` and presenting results for chosen **car make** and **model name**. 
Every new response from that site(if the car exists) is being saved within database (cars make and model name). 
The car can be `rated` from **1** to **5**. User can also see the **list of all cars**, with their current average rate, requested so far.
User can also see **5 Top Cars** which have the biggest *number of rates*.  


## Installation & Requirements
```
Python 3+, Django 3+, Django Rest Framework 3+.
```
Written on Windows 10


## Usage
-----------------------------------------------

### Adding a new Car

https://*****

- request method `POST`



*Possible answers*: 
- `200` - ok
- `400` - bad request
-----------------------------------------------

### Rating a car

https://*****

- request method `POST`
... 


*Possible answers*: 
- `200` - ok
- `400` - bad request
-----------------------------------------------

### List of all registered Cars

https://*****

- request method `GET`
...

*Possible answers*: 


-----------------------------------------------

### Top 5 most rated Cars

https://*****

- request method `GET`
...

*Possible answers*: 



-----------------------------------------------


## Authors and acknowledgment
paulina.wojno@gmail.com


## Project status
Under develop.

