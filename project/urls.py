from django.urls import path
from.views import *
urlpatterns=[
    path('form/', UserView, name='form')
]