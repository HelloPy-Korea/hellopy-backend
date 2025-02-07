from rest_framework import serializers

from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'is_deleted', 'created_at', 'updated_at']

