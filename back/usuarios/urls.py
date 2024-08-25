from django.urls import path
from .views import *
app_name = 'usuarios'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('cliente', Clientes.as_view(), name='cliente'),
]