# E-commerce Django Rest Api

Simple django web app built to use as rest api for e-commerce website with [JWT](https://pl.wikipedia.org/wiki/JSON_Web_Token) authorization

## Installation

1. Setup virtualenv
```bash
virtualenv env
source env/bin/activate
```
2. Install requirements
```bash
pip install -r requirements.txt
```
3. Create .env file in root directory and set database connection details.
Example:
```.env
SECRET_KEY = 'django-secret-key'
DEBUG = True
DATABASE_URL = localhost
DATABASE_NAME = database_name
DATABASE_USER = postgres
DATABASE_PASSWORD = postgres
```
4. Migrate
```sh
python manage.py migrate
```
5. Run
```sh
python manage.py runserver
```


## Used technologies
* [Django](https://www.djangoproject.com/): used for web app
* [django-rest-framework](https://www.django-rest-framework.org/): used for api
* [djoser](https://djoser.readthedocs.io/en/latest/index.html): used for authentication
