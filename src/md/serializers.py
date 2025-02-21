from rest_framework import serializers
from .models import Md, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class MdSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True, source="tag_set")  # ✅ source를 활용한 최적화

    class Meta:
        model = Md
        fields = ['id', 'product_name', 'image_url', 'tags']