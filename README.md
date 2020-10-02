# django-todo

Todo application, working with REST framework for Django. Each Todo item has a name, description, date of creation, status, expected finish date. 
The items track change history. A user can only view and edit his own items.

## Usage

get all todo items

/api/todo-items/

get a particular item by ID

/api/todo-items/<pk>/

