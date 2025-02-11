from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Notice
from .serializers import NoticeSerializer
# Create your views here.

class NoticeViewSet(ModelViewSet):
    serializer_class = NoticeSerializer
    
    def get_queryset(self):
        """
        ## is_deleted는 제외시켜주는 역할
        """
        return Notice.objects.filter(is_deleted=False)
    
    def list(self, request, *args, **kwargs):
        """
        ## Notice 조회 10개 씩
        pagenation : ?page=1
        """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "status": "SUCCESS",
                "error": None,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        if not queryset.exists():
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "No Data",
                    "message": "조회할 공지사항 데이터가 없습니다."
                },
                "data": []
            }, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": "SUCCESS",
            "error": None,
            "data": serializer.data,
            "pagenation": {}
        }, status=status.HTTP_200_OK)
        
    def retrieve(self, request, *args, **kwargs):
        """
        ## 특정 Notice 조회
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
                    "code": "ERROR",
                    "message": "해당 FAQ를 찾을 수 없습니다."
                    },
                "data": None
            }, status=status.HTTP_200_OK)
    def create(self, request, *arg, **kwargs):
        """
        ## Notice Create
        공지사항 생성 api
        """
        serializer = self.get_serializer(data=request.data)
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
        }, status=status.HTTP_200_OK)
    
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
            }, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "Not Found Error",
                    "message": "해당 Notice를 찾을 수 없습니다."
                }
            }, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        """
        ## notice 삭제
        """
        try:
            notice = self.get_object()
            notice.is_deleted = True
            notice.save()
            return Response({
                "status": "SUCCESS",
                "error": None,
                "message": "Notice 삭제 처리 완료"
            }, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "status": "ERROR",
                "error": {
                    "code": "Not Found",
                    "message": "해당 Notice를 찾을 수 없습니다."
                }
            }, status=status.HTTP_200_OK)