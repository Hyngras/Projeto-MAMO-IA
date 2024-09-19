from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_rest.urls')),  # Inclua as URLs da app api_rest
]
