from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    url('respaldar_restaurar/', respaldar_restaurar, name='respaldar_restaurar'),
]