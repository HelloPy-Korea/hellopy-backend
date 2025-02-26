from rest_framework import serializers

from .models import Notice


class NoticeSummarizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ["id", "title", "is_pinned"]


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ["id", "title", "content", "is_pinned", "created_at", "updated_at"]
