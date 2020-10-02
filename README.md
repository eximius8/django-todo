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

## Usage

get all todo items
```
/api/todo-items/
```
get a particular item by ID
```
/api/todo-items/<ID>/
```
