from rest_framework import serializers

from .models import PymonCalendar


class PymonCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PymonCalendar
        fields = "__all__"
