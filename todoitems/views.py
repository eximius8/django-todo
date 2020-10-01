from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response


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
        return user.todoitems.all()#TodoItem.objects.filter(owner=user).order_by('-created_date')
       
    def list(self, request):        
        serializer = TodoItemSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)