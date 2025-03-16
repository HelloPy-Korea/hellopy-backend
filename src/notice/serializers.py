from rest_framework import serializers

from .models import Notice, NoticeTag, NoticeTagRelation


class NoticeTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeTag
        fields = ["id", "name"]


class NoticeTagRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeTagRelation
        fields = ["id", "notice", "tag"]


class NoticeSummarizeListSerializer(serializers.ModelSerializer):
    tags = NoticeTagSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ["id", "title", "is_pinned", "tags"]


class NoticeSerializer(serializers.ModelSerializer):
    tags = NoticeTagSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ["id", "title", "content", "is_pinned", "tags", "created_at", "updated_at"]
