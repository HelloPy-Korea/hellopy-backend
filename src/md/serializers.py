from rest_framework import serializers

from .models import Md


class MdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Md
        fields = '__all__'