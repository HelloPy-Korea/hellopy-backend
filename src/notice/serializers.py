from rest_framework import serializers

from public.models import Tag

from .models import Notice


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "domain"]

    def create(self, validated_data):
        validated_data["domain"] = "notice"
        return super().create(validated_data)


# 목록 데이터 반환 Serializer
class NoticeSummarizeListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ["id", "title", "is_pinned", "tags"]


# 세부 공지 내용 반환 Serializer
class NoticeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ["id", "title", "content", "is_pinned", "created_at", "updated_at", "tags"]
