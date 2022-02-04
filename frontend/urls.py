from .views import *
from django.urls import path

app_name = "frontend"

urlpatterns = [
    path('', index, name="index"),
    path('matriculas', matriculas, name="matriculas"),
]
