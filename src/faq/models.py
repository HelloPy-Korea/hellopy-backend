from django.db import models

from core.mixins.models import SoftDeleteModel


class FAQ(SoftDeleteModel):
    """
    ### FAQ 필드 정의
    """

    question = models.CharField(max_length=255, verbose_name="질문")
    answer = models.TextField(verbose_name="답변")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "자주하는 질문"
        ordering = ["-created_at"]

    def __str__(self):
        return self.question
