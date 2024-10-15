from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'profile_image']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = CustomUser(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
    
        # User Informations in the token
        token['email'] = user.email
        token['username'] = user.username
        if user.role:
            token['role'] = user.role.role_name
        if user.profile_image:
            token['profile_image'] = user.profile_image.url
        
        # Log pour déboguer
        print("Token data: ", token)
        
        return token
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_image']
        
class UpdateUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image']
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        
        if 'profile_image' in validated_data:
            instance.profile_image = validated_data['profile_image']
            
        instance.save()
        
        return instance