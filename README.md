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
```
curl --header "Content-Type: application/json" --request POST\
 --data '{"username":"api-user","password":"testing321", "password_confirm":"testing321"}'\
 http://127.0.0.1:8000/accounts/register/
```
Response:
```
{"id":5,"username":"testuser","first_name":"","last_name":"","email":""}
```
### Login

```
curl --header "Content-Type: application/json" --request POST\
 --data '{"login":"api-user","password":"testing321"}'\
 http://127.0.0.1:8000/accounts/login/
```
Response:
```
{"detail":"Login successful","token":"88268a1384ca93ca03845578bc0daa7ef90817df"}
```
### Logout

```
curl -X POST http://127.0.0.1:8000/accounts/logout/\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```
Response:
```
{"detail":"Logout successful"}
```

### Create new TodoItem

```
curl -X POST http://127.0.0.1:8000/api/todo-items/\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'\
 --header "Content-Type: application/json"\
 --data '{"name":"Todo item 1", "description":"Description todo item 1", "expected_finish_date":null, "status":"N"}'
```
Response:
```
{
    "id":4,
    "name":"Todo item 1",
    "description":"Description todo item 1",
    "created_date":"2020-10-03T20:06:14.472946Z",
    "expected_finish_date":null,
    "status":"N"
}
```

### See my TodoItems

```
curl -X GET http://127.0.0.1:8000/api/todo-items/\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```
Response:
```
[
    {
        "id":4,
        "name":"Todo item 1",
        "description":"Description todo item 1",
        "created_date":"2020-10-03T20:06:14.472946Z",
        "expected_finish_date":null,
        "status":"N"
    }
]
```
#### Filter by status or by expected finish data
For details check [views.py](https://github.com/eximius8/django-todo/blob/master/todoitems/views.py)
By status
```
curl -X GET http://127.0.0.1:8000/api/todo-items/?status=N\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```
By finish date - date is null 
```
curl -X GET "http://127.0.0.1:8000/api/todo-items/?null=t"\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```
By finish date - date from to
```
curl -X GET "http://127.0.0.1:8000/api/todo-items/?start=2010-01-01&end=2021-01-01/"\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```

### See particular item

```
curl -X GET http://127.0.0.1:8000/api/todo-items/4/\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'
```
Response. History is implemented with [django-simple-history](https://pypi.org/project/django-simple-history/)
```
{
    "name":"Todo item 1",
    "description":"Description todo item 1",
    "created_date":"2020-10-03T20:06:14.472946Z",
    "expected_finish_date":null,
    "status":"N",
    "history":[
        {
            "id":4,
            "name":"Todo item 1",
            "description":"Description todo item 1",
            "created_date":"2020-10-03T20:06:14.472946Z",
            "expected_finish_date":null,
            "status":"N",
            "owner_id":4,
            "history_id":5,
            "history_date":"2020-10-03T20:06:14.476899Z",
            "history_change_reason":null,
            "history_type":"+",
            "history_user_id":4
        }]
}
```
### Change Todo item

```
curl -X PUT http://127.0.0.1:8000/api/todo-items/4/\
 -H 'Authorization: Token 88268a1384ca93ca03845578bc0daa7ef90817df'\
 --header "Content-Type: application/json"\
 --data '{"name":"Updated Todo item 1", "description":"Updated description todo item 1", "expected_finish_date":"2020-10-20", "status":"P"}'
```
Response
```
{
    "id":4,
    "name":"Updated Todo item 1",
    "description":"Updated description todo item 1",
    "created_date":"2020-10-03T20:06:14.472946Z",
    "expected_finish_date":"2020-10-20",
    "status":"P"
}
```
