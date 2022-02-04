from .views import index
from django.urls import path, include

app_name = "frontend"

urlpatterns = [
    path('', index, name="index"),
]
