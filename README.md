# WeatherAPI
It returns weather information given country and city parameters
```http
GET /weather?city=$City&country=$Country
```
## Prerequisites
Requires Python3 v3.9.6+ to run.
Install Pyenv packaging tool.
```sh
python3 -m pip install pipenv
```

### Redis for cache
To install Redis follow the instructions according your OS.
https://redis.io/docs/getting-started/installation/

## Setup
To run locally clone the repository.
Go inside the project folder and install the dependencies using pipenv:
```sh
pipenv sync
```

Activate the enviroment:
```sh
pipenv shell
```
Add secrets, copy the example.env file and rename it to .env and then fill in the secrets
```
URL="PUT HERE YOUR WEATHER URL SERVICE"
APP_ID="PUT HERE YOUR SECRET KEY"
```
Run the next command:
```sh
 uvicorn main:app 
```

Then open in your browser the following url: ```http://127.0.0.1:8000```,
example endpoint:
```http://127.0.0.1:5000/weather?city=Bogota&country=co```



Deactivate the virtual env
```sh
 deactivate 
```

## Linter
Run static analysis code
```
 flake8 app/* 
```

## Testing

Run unit test and integration test
```sh
 pytest 
```
Test coverage
```sh
 coverage run -m pytest tests/unit_test 
```

## Documentation
Open endpoint documentation in OpenAPI 
```sh
 http://127.0.0.1:8000/docs 
```




