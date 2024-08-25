from django.urls import path
from .views import *
app_name = 'productos'

urlpatterns = [
    path('producto', Productos.as_view(), name='producto'),
]