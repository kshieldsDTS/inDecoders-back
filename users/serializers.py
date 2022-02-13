from djoser.serializers import UserCreateSerializer
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
            'password',
            'avatar',
            'skills',
            'portfolio',
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'payrate'
        )

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'avatar',
            'skills',
            'portfolio',
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'payrate'
        )
