from rest_framework import serializers

from public.models import ActivityTag
from public.serializers import TagSerializer

from .models import ActionPhoto, ActivityAction


# 액션과 연결된 사진 정보를 직렬화하는 Serializer
class ActionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPhoto
        fields = ["id", "image"]  # 사진 ID와 이미지 경로 포함


# 액션과 태그 간의 관계를 직렬화하는 Serializer
class ActivityTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTag
        fields = ["id", "activity_action", "tag"]  # 관계 테이블의 ID, 액션 ID, 태그 ID 포함


# 목록 조회 시 최소한의 데이터만 반환하는 Serializer
class ActivityActionListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # 액션에 연결된 태그 목록 포함

    class Meta:
        model = ActivityAction
        fields = ["id", "title", "thumbnail", "tags"]  # 목록 조회 시 content와 photos 제외


# 상세 조회 시 모든 정보를 반환하는 Serializer
class ActivityActionDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # 태그 목록 포함
    photos = ActionPhotoSerializer(many=True, read_only=True)  # 연결된 사진 목록 포함

    class Meta:
        model = ActivityAction
        fields = [
            "id",
            "title",
            "thumbnail",
            "content",
            "tags",
            "photos",
        ]  # 상세 조회 시 모든 정보 포함
