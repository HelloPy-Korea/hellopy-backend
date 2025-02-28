from rest_framework import serializers

from .models import ActionPhoto, CommunityAction, CommunityTag, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ActionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPhoto
        fields = ["id", "image"]


class CommunityTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityTag
        fields = ["id", "community_action", "tag"]


class CommunityActionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    photos = ActionPhotoSerializer(many=True, read_only=True)
    tag_ids = serializers.ListField(
        write_only=True, child=serializers.IntegerField(), required=False
    )
    photo_files = serializers.ListField(
        write_only=True, child=serializers.ImageField(), required=False
    )

    class Meta:
        model = CommunityAction
        fields = ["id", "title", "content", "tags", "photos", "tag_ids", "photo_files"]

    def create(self, validated_data):
        tag_ids = validated_data.pop("tag_ids", [])
        photo_files = validated_data.pop("photo_files", [])

        community_action = CommunityAction.objects.create(**validated_data)

        for tag_id in tag_ids:
            CommunityTag.objects.create(community_action=community_action, tag_id=tag_id)

        for photo in photo_files:
            ActionPhoto.objects.create(community_action=community_action, image=photo)

        return community_action
