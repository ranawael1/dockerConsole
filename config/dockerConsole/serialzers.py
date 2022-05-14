from rest_framework import serializers
from .models import Container




class ContainersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ['id', 'name','tag', 'user']