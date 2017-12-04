import djoser.views
from django.http import JsonResponse
from rest_framework import serializers, generics, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from djoser.conf import settings

class CustomRegistrationView(generics.CreateAPIView):
    serializer_class = settings.SERIALIZERS.user_create
    permission_classes = [permissions.AllowAny]
    queryset = ''

    def perform_create(self, serializer):
        try:
            user_type = self.request.data['user_type']
        except Exception as e:
            raise serializers.ValidationError(
                "User type is missing!"
            )
        if user_type is not None:
            user = serializer.save()
