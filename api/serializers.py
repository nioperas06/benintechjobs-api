from .models import Job, Quote
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company', 'email', 'url', 'title', 'location', 'description', 'logo', 'created_at')


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'name', 'email', 'phone', 'description')
