from django.test import TestCase
from django.contrib.auth.models import User

from datetime import datetime


from todoitems.models import TodoItem



class TodoItemModelTests(TestCase):

    def test_todo_item_models_creation(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # create user
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        # create todoitem
        self.todoitem = TodoItem.objects.create(owner = self.user, 
                                                name = "Todo item test 1",
                                                description = "Todo item test 1 description")
        
        self.assertIs(self.todoitem.status, "N")
        self.assertFalse(self.todoitem.expected_finish_date)
        self.assertIs(self.todoitem.owner, self.user)
        self.assertIs(self.todoitem.name, "Todo item test 1")
        self.assertIs(self.todoitem.history.count(), 1)

        self.todoitem.expected_finish_date = datetime.now().date()
        self.todoitem.save()
        self.assertIs(self.todoitem.history.count(), 2)

        self.assertTrue(self.todoitem.expected_finish_date)
