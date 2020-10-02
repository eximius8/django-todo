from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response

from datetime import datetime, timedelta


# local imports
from todoitems.serializers import TodoItemSerializer
from todoitems.models import TodoItem



class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API for todo Items
    """   
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated,]
    

    def get_queryset(self):
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
        serializer = TodoItemSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)