import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    # Clase de bienvenida y los endpoints
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        # Retorna lista de caracteristicas de la API
        an_apiview = [
            'GET, POST, PATH, PUT, DELETE'
        ]

        return Response({'message': 'Welcome to api', 'an_apiview': an_apiview})
    
    def post(self, request):
        # Crea un mensaje con un input
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        #Actualiza un objeto
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        # actualización parcial de un objeto
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        # borra  un objeto
        return Response({'method': 'DELETE'})