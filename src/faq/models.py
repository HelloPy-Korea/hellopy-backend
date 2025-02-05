from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    ## 공통 필드 모델 관리
    1. id : 게시물의 고유 id
    2. Status : 게시물의 상태
    """
    id = models.AutoField(primary_key=True)
    class Status(models.TextChoices):
        NORMAL = 'normal', '게시됨'
        HIDDEN = 'hidden', '숨김'
        DELETE = 'deleted', '삭제됨'
    
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.NORMAL,
        verbose_name="게시물 상태"
    )
    
    class Meta:
        # 데이터베이스 추상 모델
        abstract = True

class FAQ(BaseModel):
    class QuestionType(models.TextChoices):
        ACTIVITY = 'activity', '활동'
        CONFERENCE = 'conference', '기타등등'   
    question = models.CharField(max_length=255, verbose_name="질문")
    answer = models.TextField(verbose_name="답변")
    question_type = models.CharField(
        max_length=20, 
        choices=QuestionType.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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

