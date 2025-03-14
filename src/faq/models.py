from django.db import models


class FAQ(models.Model):
    """
    ### FAQ 필드 정의
    """

    is_deleted = models.BooleanField(default=False, verbose_name="숨김 여부")
    question = models.CharField(max_length=255, verbose_name="질문")
    answer = models.TextField(verbose_name="답변")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "자주하는 질문"

    def __str__(self):
        return self.question
