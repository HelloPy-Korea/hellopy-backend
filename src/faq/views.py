from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from .models import FAQ
from .serializers import FAQSerializer


# Create your views here.
# 예상 CRUD
@extend_schema_view(
    list=extend_schema(summary="FAQ 목록 조회", description="등록된 FAQ 목록을 조회합니다."),
    retrieve=extend_schema(summary="FAQ 상세 조회", description="특정 FAQ의 상세정보를 조회"),
    create=extend_schema(summary="FAQ 생성", description="새로운 FAQ를 생성합니다."),
    update=extend_schema(summary="FAQ 수정", description="기존 FAQ 정보를 수정합니다."),
    partial_update=extend_schema(summary="FAQ 부분 수정", description="FAQ 일부 정보를 수정합니다."),
    destroy=extend_schema(summary="FAQ 삭제", description="FAQ 데이터를 삭제 처리합니다."),
)
class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer