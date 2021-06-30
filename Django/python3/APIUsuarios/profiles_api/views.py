from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import serializers, models, permissions



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


class HelloViewSet(viewsets.ViewSet):
    # Test API ViewSet
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        a_viewset = [
            'Test de API ViewSet para list, create, retrieve, update',
            'Automaticamente mapea a los URLS usando RRouters'
        ]
        return Response({'message': 'Hola ', 'a_viewset': a_viewset})
    
    def create(self, request):
        # crear nuevo mensaje
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'massage': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        # Optiene un objecto por id
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        return Response({'http_method': 'PATH'})
    
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    #Crear y actualizar perfiles

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filters_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    # Crea tokens de autorización para los usuarios
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    # Feed para crear, leer, actualizar el feed
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        # Setea el perfil de usuario para el usuario logueado
        serializer.save(user_profile=self.request.user)