# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField(read_only=True)  # Add token field

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2', 'bio', 'token')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Remove password2 as it's not part of the model
        validated_data.pop('password2')
        
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            bio=validated_data.get('bio', '')
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        # Create token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        return user

    def to_representation(self, instance):
        """Override to include the token in the response"""
        ret = super().to_representation(instance)
        token, created = Token.objects.get_or_create(user=instance)
        ret['token'] = token.key
        return ret

class UserLoginSerializer(serializers.Serializer):
    """Serializer for user login and token retrieval"""
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # Add token field

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        attrs['user'] = user
        # Create token for the user
        token, created = Token.objects.get_or_create(user=user)
        attrs['token'] = token.key
        return attrs

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile"""
    follower_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                  'bio', 'profile_picture', 'follower_count', 'following_count',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')