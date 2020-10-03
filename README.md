# django-todo

Todo application, working with REST framework for Django. Each Todo item has a name, description, date of creation, status, expected finish date.
The items track change history. A user can only view and edit his own items.

## Install

Run docker-compose to build database (postgres) and web services
```
docker-compose build
```

Migrate to create database and create superuser

```
sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py createsuperuser
```

Run image

```
docker-compose up
```

View logs from django:
```
docker-compose logs -f web
```

## Usage

Registration and login are implemented with [django-rest-registration](https://pypi.org/project/django-rest-registration/)

### Register
'''
curl --header "Content-Type: application/json" --request POST --data '{"username":"api-user","password":"testing321", "password_confirm":"testing321"}' http://127.0.0.1:8000/accounts/register/
'''

{"id":5,"username":"testuser","first_name":"","last_name":"","email":""}

### Login

```
curl --header "Content-Type: application/json" --request POST --data '{"login":"api-user","password":"testing321"}' http://127.0.0.1:8000/accounts/login/
```

{"detail":"Login successful","token":"88268a1384ca93ca03845578bc0daa7ef90817df"}

### Logout

```
curl -X POST http://127.0.0.1:8000/accounts/logout/ -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```

{"detail":"Logout successful"}

get all todo items
```
/api/todo-items/
```
get a particular item by ID
```
/api/todo-items/<ID>/
```
