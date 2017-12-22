from rest_framework_jwt.views import obtain_jwt_token
from authentication.views import CustomRegistrationView
from django.urls import path, include
from djoser import views

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    path('auth/login/', obtain_jwt_token),
    path('auth/register/', CustomRegistrationView.as_view()),
    path('auth/password/reset/', views.PasswordResetView.as_view()),
]
