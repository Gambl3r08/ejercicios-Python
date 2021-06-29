from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    #Campos
    name = serializers.CharField()