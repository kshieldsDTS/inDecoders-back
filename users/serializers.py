from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models
from .models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = (
            'id',
            'email',
            'username',
            'bio',
            'skills',
            'portfolio',
            'payrate',
        )

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'bio',
            'skills',
            'portfolio',
            'payrate',
        )
