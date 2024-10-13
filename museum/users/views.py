from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
import logging
from .serializers import UserSerializer, CustomTokenObtainPairSerializer

logger = logging.getLogger(__name__)

# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, email=username, password=password)
        if user is not None:
            token_data = CustomTokenObtainPairSerializer.get_token(user)
            return Response({
                'refresh': str(token_data),
                'access': str(token_data.access_token),
                'user_data': {
                    'email': user.email,
                    'username': user.username,
                    'role': user.role.role_name if user.role else None,
                    'profile_image': user.profile_image.url if user.profile_image else None
                }
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)