from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    code = serializers.CharField()
    message = serializers.CharField()

    def to_representation(self, instance):
        return {
            "code": instance.code,
            "message": instance.message,
        }


class PageNumberPaginationSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField()
    previous = serializers.CharField()

    def to_representation(self, instance):
        return {
            "count": instance.count,
            "next": instance.next,
            "previous": instance.previous,
        }


class SuccessResponseSerializer(serializers.Serializer):
    status = serializers.CharField(default="SUCCESS")
    data = serializers.DictField(required=False)
    pagination = PageNumberPaginationSerializer(required=False, allow_null=True)

    def to_representation(self, instance):
        return {
            "status": instance.status,
            "data": instance.data,
            "error": None,
            "pagination": None,
        }


class ListSuccessResponseSerializer(serializers.Serializer):
    status = serializers.CharField(default="SUCCESS")
    data = serializers.ListField(required=False, child=serializers.DictField())
    pagination = PageNumberPaginationSerializer(required=False, allow_null=True)

    def to_representation(self, instance):
        return {
            "status": instance.status,
            "data": instance.data,
            "error": None,
            "pagination": instance.pagination,
        }


class ErrorResponseSerializer(serializers.Serializer):
    status = serializers.CharField(default="ERROR")
    error = ErrorSerializer()

    def to_representation(self, instance):
        return {
            "status": instance.status,
            "error": instance.error,
            "data": None,
            "pagination": None,
        }
