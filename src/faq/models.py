from django.db import models

from core.mixins.models import SoftDeleteModel


class FAQ(SoftDeleteModel):
    """
    ### FAQ 필드 정의
    """

    question = models.CharField("질문", max_length=255)
    answer = models.TextField("답변")
    is_visible = models.BooleanField("공개 여부", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["-created_at"]

    def __str__(self):
        return self.question
