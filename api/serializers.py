from .models import Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company', 'email', 'url', 'title', 'location', 'description', 'logo', 'created_at')
