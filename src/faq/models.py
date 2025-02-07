from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    ## 공통 필드 모델 관리
    1. id : 게시물의 고유 id
    2. Status : 게시물의 상태
    """
    id = models.AutoField(primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # 데이터베이스 추상 모델
        abstract = True

class FAQ(BaseModel):
    """
    ### FAQ 필드 정의
    """
    is_deleted = models.BooleanField(default=False, verbose_name="삭제 여부")
    question = models.CharField(max_length=255, verbose_name="질문")
    answer = models.TextField(verbose_name="답변")
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    def __str__(self):
        return self.question

class Notice(BaseModel):
    title=models.CharField(max_length=255, verbose_name="공지 제목")
    content = models.TextField(verbose_name="공지 내용")
    
    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항 목록"
        
    def __str__(self):
        return self.title

