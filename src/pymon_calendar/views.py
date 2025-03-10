from django.utils.dateparse import parse_date
from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import PymonCalendar
from .serializers import PymonCalendarSerializer
from .swagger import PymonCalendarAPIDocs


@extend_schema_view(list=PymonCalendarAPIDocs.list())
class PymonCalendarViewSet(GenericViewSet):
    serializer_class = PymonCalendarSerializer

    def get_queryset(self):
        queryset = PymonCalendar.objects.all().order_by(
            "-year_month"
        )  # 최신 데이터가 먼저 오도록 정렬
        year_month = self.request.query_params.get("year_month")

        if year_month:
            parsed_date = parse_date(year_month + "-01")
            if parsed_date:
                queryset = queryset.filter(year_month=parsed_date)

        return queryset

    def list(self, request, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(serializer.data)
