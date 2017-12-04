from rest_framework_jwt.views import obtain_jwt_token
from authentication import views
from django.urls import path, include

urlpatterns = [
    # url(r'^auth/', include('djoser.urls')),
    path('auth/login/', obtain_jwt_token),
    path('auth/register/', views.CustomRegistrationView.as_view()),
]
