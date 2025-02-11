from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notice
        fields = ['title', 'content', 'is_deleted', 'is_pinned', 'created_at', 'updated_at']