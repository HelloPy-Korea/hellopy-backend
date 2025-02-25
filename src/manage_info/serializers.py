from rest_framework import serializers

from .models import ManagementInfo


class ManagementInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementInfo
        fields = '__all__'