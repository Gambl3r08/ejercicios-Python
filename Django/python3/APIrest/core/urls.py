from django.urls import path
from core.views import *
urlpatterns = [
    path('getuser/<int:idUser>/', getUser, name='getuser'),
    path('setuser', createUser, name='setuser')
]