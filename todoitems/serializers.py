from rest_framework import serializers
from todoitems.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['name', 'description', 'created_date', 'expected_finish_date', 'status']
