from django.db import models
from simple_history.models import HistoricalRecords


class TodoItem(models.Model):
    """
    todo item class
    """

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=3000, blank=False)
    owner = models.ForeignKey('auth.User', related_name='todoitems', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=False)
    expected_finish_date = models.DateTimeField(blank=True, null=True)
    CHOICES = (
        ('N', 'Новая'),
        ('P', 'Запланированная'),
        ('W', 'в Работе'),
        ('F', 'Завершённая'),        
    )
    status = models.CharField(max_length=1, blank=False, default = 'N', choices=CHOICES)

    history = HistoricalRecords()


    def __str__(self):
        return self.name
