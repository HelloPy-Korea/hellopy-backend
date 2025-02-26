from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import ManagementInfo
from .serializers import ManagementInfoSerializer


class ManagementInfoViewSet(ReadOnlyModelViewSet):
    """
    운영진을 크게 볼일은 없을거라 판단하고 retrieve는 제외시킴
    """

    queryset = ManagementInfo.objects.all()
    serializer_class = ManagementInfoSerializer

    def list(self, requset, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {
                    "status_code": "200",
                    "body": {
                        "code": "success",
                        "message": "운영자 데이터가 없습니다",
                        "data": [],
                        "pagination": {},
                    },
                },
                status=status.HTTP_200_OK,
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "status_code": "200",
                "body": {
                    "code": "success",
                    "message": "성공",
                    "data": serializer.data,
                    "pagination": {},
                },
            },
            status=status.HTTP_200_OK,
        )
