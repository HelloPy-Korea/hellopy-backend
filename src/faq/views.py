from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.exceptions import NotFound

class FAQPagination(PageNumberPagination):
    """
    ## DEFAULT_SETTING
    - 한 페이지 : 10
    - 한 번 요청의 최대 크기 : 100
    ex)
    bash
    curl -X GET "http://hello-py.com:8080/api/faqs/?page=1&page_size=150"
    -> 반환되는 data의 개수는 100개
    더 많은 요청시 수정
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100  # page 단위의 요청 최대 size 

class FAQViewSet(ModelViewSet):
    serializer_class = FAQSerializer
    pagination_class = FAQPagination  # ✅ 페이지네이션 클래스 적용

    def get_queryset(self):
        """
        ## queryset에서 is_deleted는 제외시켜주는 역할
        """
        return FAQ.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        """
        ## 모든 FAQ 목록 조회
        ### 특징 : is_deleted는 제외
        """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  # ✅ 페이지네이션 적용
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "status": "SUCCESS",
                "error": None,
                "data": serializer.data
            })
        
        if not queryset.exists():
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "No Data",
                    "message": "조회할 FAQ 데이터가 없습니다."
                },
                "data": []
            }, status=status.HTTP_202_ACCEPTED)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": "SUCCESS",
            "error": None,
            "data": serializer.data,
            "pagination": {}
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        ## 특정 FAQ 조회
        """
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "status": "SUCCESS",
                "error": None,
                "data": serializer.data,
            }, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "Not Found",
                    "message": "해당 FAQ를 찾을 수 없습니다."
                },
                "data": None
            }, status=status.HTTP_202_ACCEPTED)

    def create(self, request, *args, **kwargs):
        """
        ## 새로운 FAQ 생성
        - HelloPy 초기 홈페이지를 위한 api 아니며 
          추후 createㅏ 페이지 생성을 고려한 함수
        - 성공시 status : SUCCESS
        - 실패시 status : ERROR
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "SUCCESS",
                "error": None,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "ERROR",
            "error": {
                "code": "Validation Error",
                "message": serializer.errors
            }
        }, status=status.HTTP_202_ACCEPTED)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "SUCCESS",
                    "error": None,
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "Validation Error",
                    "message": serializer.errors
                }
            }, status=status.HTTP_202_ACCEPTED)
        except NotFound:
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "Not Found",
                    "message": "해당 FAQ를 찾을 수 없습니다."
                }
            }, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, *args, **kwargs):
        """
        ## FAQ 삭제 (Soft Delete)
        - 실제 삭제가 아닌 `is_deleted=True`로 변경
        """
        try:
            faq = self.get_object()
            faq.is_deleted = True
            faq.save()
            return Response({
                "status": "SUCCESS",
                "error": None,
                "message": "FAQ 삭제 처리 완료"
            }, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "Not Found",
                    "message": "해당 FAQ를 찾을 수 없습니다."
                }
            }, status=status.HTTP_202_ACCEPTED)