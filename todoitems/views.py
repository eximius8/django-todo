from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response

from datetime import datetime


# local imports
from todoitems.serializers import TodoItemSerializer, TodoItemListSerializer
from todoitems.models import TodoItem



class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API for todo Items
    """
    serializer_class = TodoItemListSerializer
    permission_classes = [permissions.IsAuthenticated,]


    def get_queryset(self):
        """
        Several query parameters can be specified in url:
            status - filters by status of TodoItem:
                    ('N', 'Новая'), ('P', 'Запланированная'), ('W', 'в Работе'), ('F', 'Завершённая')
            null - filters TodoItem with no record of expected_finish_date (= null)
            start - date in the form "YYYY-mm-dd" (2020-12-31) returns query with expected_finish_date of TodoItem greater than start
            end - same as start but expected_finish_date is lower than end
            if both start and end are provided returns query with expected_finish_date between start and end
            If start only is given

            example:
            http://example.com/api/todo-items/?status=P&start=2020-08-01&end=2021-01-01
            will return all TodoItems with status ('P', 'Запланированная') and expected_finish_date between 1 August 2020 and 1January 2021

        """
        user = self.request.user
        user_todo_items = user.todoitems.all()
        status = self.request.query_params.get('status', None)
        is_null = self.request.query_params.get('null', None)
        if status is not None:
            user_todo_items = user_todo_items.filter(status=status)
        if is_null is not None:
            user_todo_items = user_todo_items.filter(expected_finish_date__isnull=True)
        else:
            try:
                start = datetime.strptime(self.request.query_params.get('start', None), "%Y-%m-%d").date()
            except:
                start = None
            try:
                end = datetime.strptime(self.request.query_params.get('end', None), "%Y-%m-%d").date()
            except:
                end = None

            if start is not None and end is not None:
                user_todo_items = user_todo_items.filter(expected_finish_date__range=(start, end))
            elif start is not None:
                user_todo_items = user_todo_items.filter(expected_finish_date__gte=start)
            elif end is not None:
                user_todo_items = user_todo_items.filter(expected_finish_date__lte=end)

        return user_todo_items#TodoItem.objects.filter(owner=user).order_by('-created_date')

    def list(self, request):
        serializer = TodoItemListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TodoItemSerializer # different serializer for detailviews
        return super(TodoItemViewSet, self).retrieve(request, *args, **kwargs)
