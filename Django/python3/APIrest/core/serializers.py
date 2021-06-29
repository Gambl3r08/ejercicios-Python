from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name  = serializers.CharField()
    user = serializers.CharField()
    password = serializers.CharField()


    def create(self, validated_data):
        return User.objects.create(**validated_data)
    

    def update(self, instance: User, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.user = validated_data.get('user', instance.user)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance