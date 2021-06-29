from django.http.request import HttpRequest
from django.http.response import  JsonResponse
from django.shortcuts import render
from core.models import User
from core.serializers import UserSerializer


def getUser(request, idUser):
    user = User.objects.get(id=idUser)
    serializer = UserSerializer(user)
    
    return JsonResponse({'data': serializer.data})

def createUser(request):
    pass
