from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Merchandise
from .serializers import MerchandiseSerializer


class MerchandiseViewSet(ReadOnlyModelViewSet):
    """
    MD 페이지는 상세보기 페이지가 존재하지 않으므로 retrieve는 생략되었습니다.
    """

    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {
                    "status_code": "200",
                    "body": {
                        "code": "success",
                        "message": "MD 데이터가 존재하지 않습니다",
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
