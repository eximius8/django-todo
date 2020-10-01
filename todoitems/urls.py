from django.urls import include, path

from rest_framework import routers

from todoitems.views import TodoItemViewSet


router = routers.DefaultRouter()
router.register(r'todo-items', TodoItemViewSet, basename='TodoItem')



urlpatterns = [    
    path('', include(router.urls)),
]