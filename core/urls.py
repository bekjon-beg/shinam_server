from django.urls import path
from .views import *

urlpatterns = [
    path('put/', usercreate, name='create'),
]