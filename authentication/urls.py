from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from authentication import views

urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/login/', obtain_jwt_token),
]
