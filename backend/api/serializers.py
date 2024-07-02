from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {"password": {"write_only": True, "required": True}}
        
        
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
        



class notesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'author', 'title', 'content', 'created_at']
        extra_kwargs = {"author": {"read_only": True}}        