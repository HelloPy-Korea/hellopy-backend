from rest_framework import serializers

from .models import ActionPhoto, ActivityAction, ActivityTag, ActivityTagRelation


class ActivityTagSerializer(serializers.ModelSerializer):
    """태그 정보를 직렬화하는 Serializer"""

    class Meta:
        model = ActivityTag
        fields = ["id", "name"]  # 태그 ID와 이름 포함


class ActionPhotoSerializer(serializers.ModelSerializer):
    """액션과 연결된 사진 정보를 직렬화하는 Serializer"""

    class Meta:
        model = ActionPhoto
        fields = ["id", "image"]


class ActivityTagRelationSerializer(serializers.ModelSerializer):
    """액션과 태그 간의 관계를 직렬화하는 Serializer"""

    class Meta:
        model = ActivityTagRelation
        fields = ["id", "activity_action", "tag"]


class ActivityActionListSerializer(serializers.ModelSerializer):
    """목록 조회 시 최소한의 데이터만 반환하는 Serializer"""

    tags = ActivityTagSerializer(many=True, read_only=True)

    class Meta:
        model = ActivityAction
        fields = ["id", "title", "thumbnail", "tags"]


class ActivityActionDetailSerializer(serializers.ModelSerializer):
    """상세 조회 시 모든 정보를 반환하는 Serializer"""

    tags = ActivityTagSerializer(many=True, read_only=True)
    photos = ActionPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = ActivityAction
        fields = ["id", "title", "thumbnail", "content", "tags", "photos"]
