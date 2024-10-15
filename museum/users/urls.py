from django.urls import path
from .views import SignUpView, LoginView, UpdateProfileView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/profile/update/<int:pk>/', UpdateProfileView.as_view(), name='profile-update'),
    # Routes pour tokens JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
