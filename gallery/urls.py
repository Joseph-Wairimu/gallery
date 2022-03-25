from django.urls import path,register_converter
from django.conf import settings

from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
   
]