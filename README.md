# WeatherAPI
<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-python-success?logo=python&logoColor=white"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/python-v3.9.6%2B-blue"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/pytest-testing%2B-yellowgreen"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/flake8-Code%20analisys-green"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/asyncio-async%20request-orange"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/FastAPI-apis-brightgreen"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/Redis-cache-lightgrey"></a>
<a href="https://pypi.org/project/gitignoregh"><img alt="Python Versions" src="https://img.shields.io/badge/pipenv-environment-yellow"></a>




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
To install Redis follow the instructions according your OS, ensure also you start redis 
https://redis.io/docs/getting-started/installation/

## Setup
To run locally clone the repository.
Go inside the project folder and install the dependencies using pipenv:
```sh
pipenv sync
```

Activate the enviroment:
```sh
pipenv install
```
Add secrets, copy the example.env file and rename it to .env and then fill in the secrets,
if you need to change the cache time put the time in seconds in the variable ```CACHE_TIME_SECONDS```
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
```http://127.0.0.1:8000/weather?city=Bogota&country=co```



Deactivate the virtual env
```sh
 deactivate 
```

## Testing

Run unit test and integration test
```sh
 pytest 
```
or
```sh
 python -m pytest 
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

## Linter
Run static analysis code
```
 flake8 app/* 
```

or

```
 python -m flake8 app/*
```




