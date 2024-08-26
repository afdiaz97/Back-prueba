from django.urls import path
from .views import *
app_name = 'usuarios'

urlpatterns = [
    path('ventas', Ventas.as_view(), name='ventas'),
    path('detailventa',Addventa.as_view(),name="detail")
]