from django.shortcuts import render
from django.contrib.auth.models import User
#from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


# local imports
from .serializers import TodoItemSerializer
from .models import TodoItem



class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API for todo Items
    """   
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TodoItem.objects.filter(owner=user).order_by('-created_date')
       
    def list(self, request):        
        serializer = TodoItemSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        pass