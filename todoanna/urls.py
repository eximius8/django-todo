
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
    path('api/', include('todoitems.urls')),
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
