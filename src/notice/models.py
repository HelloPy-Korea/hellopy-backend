from django.core.exceptions import ValidationError
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from core.tag.models import TagModel


class NoticeTag(TagModel, models.Model):
    """공지사항 태그 모델"""

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "공지사항 태그 관리"


class NoticeTagRelation(models.Model):
    """공지사항과 태그를 연결하는 중간 모델"""

    notice = models.ForeignKey("Notice", on_delete=models.CASCADE, related_name="notice_tags")
    tag = models.ForeignKey(NoticeTag, on_delete=models.CASCADE, related_name="tag_relations")

    class Meta:
        unique_together = ("notice", "tag")  # 중복 태그 방지

    def __str__(self):
        return "공지 태그"


class Notice(models.Model):
    title = models.CharField("제목", max_length=255)
    content = CKEditor5Field("본문", config_name="extends", null=False, blank=False)
    is_deleted = models.BooleanField("삭제 여부", default=False)
    is_pinned = models.BooleanField("상단 고정", default=False)
    created_at = models.DateTimeField("등록 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)
    tag = models.ManyToManyField(NoticeTag, through="NoticeTagRelation", related_name="notices")

    def clean(self):
        from bs4 import BeautifulSoup

        # HTML 태그 제거 테스트 추출
        soup = BeautifulSoup(self.content, "html.parser")

        if not soup.get_text(strip=True):
            raise ValidationError({"content": "내용을 입력해주세요."})

    class Meta:
        verbose_name = "notice"
        verbose_name_plural = "공지사항"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Notice(id={self.id}, title={self.title})"
