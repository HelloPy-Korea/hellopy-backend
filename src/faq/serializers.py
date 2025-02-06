from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    
    @extend_schema_field(serializers.CharField())
    def get_status_display(self, obj):
        return obj.get_status_display()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_type', 'status', 'status_display', 'created_at', 'updated_at']
        
