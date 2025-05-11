from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'role']
        read_only_fields = ['id', 'is_staff', 'is_active', 'role']  # optional: make 'role' read-only if only admin sets it
