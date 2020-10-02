from rest_framework import serializers
from todoitems.models import TodoItem

# https://stackoverflow.com/questions/40736838/getting-rest-history-from-django-simple-history
class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())


class TodoItemListSerializer(serializers.ModelSerializer):
    """
    serializer for list of TodoItems - includes id to build links
    """

    class Meta:
        model = TodoItem
        fields = ['id', 'name', 'description', 'created_date', 'expected_finish_date', 'status',]

class TodoItemSerializer(serializers.ModelSerializer):
    """
    serializer for detail TodoItem - includes history but not id
    """

    history = HistoricalRecordField(read_only=True)

    class Meta:
        model = TodoItem
        fields = ['name', 'description', 'created_date', 'expected_finish_date', 'status', 'history']
