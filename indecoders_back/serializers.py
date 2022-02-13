from rest_framework import serializers
from .models import LFHelp, LFWork

class LFWorkSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = LFWork
        fields = (
            'id', 
            'owner',
            'email',
            'skills',
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'availability',
            'payrate_desired',
        )

class LFHelpSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    contact = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = LFHelp
        fields = (
            'id', 
            'owner',
            'project_name',
            'description',
            'contact',
            'skills_desired',
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'availability_desired',
            'timeline',
            'payrate'
        )