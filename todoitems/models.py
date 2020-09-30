from django.db import models
from django.contrib.auth.models import User

class TodoItem(moodels.Model):
    """
    todo item class
    """

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=3000, blank=False)
    owner = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True, blank=False)
    expected_finish_date = models.DateTimeField(blank=True, null=True)

    CHOICES = (
        ('N', 'Новая'),
        ('P', 'Запланированная'),
        ('W', 'в Работе'),
        ('F', 'Завершённая'),        
    )

    status = models.ChoiceField(blank=False, default = 'N', choices=CHOICES)
