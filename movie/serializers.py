from .models import Movie, Timestamps, PendingTimestamps, Verification
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TimestampsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestamps
        fields = '__all__'
        read_only_fields = ['movie', 'added_at']

class PendingTimestampsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingTimestamps
        fields = '__all__'
        read_only_fields = ['movie', 'added_at']

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = '__all__'
        read_only_fields = ['mod', 'timestamp', 'verified_at']
        