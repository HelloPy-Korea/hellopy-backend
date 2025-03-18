from django.db import models


class Tag(models.Model):
    DOMAIN_CHOICES = [
        ("activity", "Activity"),
        ("notice", "Notice"),
        ("default", "Default"),  # default 라는 선택지를 추가
    ]

    name = models.CharField("태그", max_length=100, unique=True)
    domain = models.CharField("도메인", max_length=10, choices=DOMAIN_CHOICES, default="default")

    class Meta:
        unique_together = ("name", "domain")
        verbose_name = "전체 태그 관리"
        verbose_name_plural = "전체 태그 관리"

    def __str__(self):
        """
        f스트링 사용 이유 : tag에 빈값(migration 이전 null 값들)이 들어간 경우
        default 부분인 점을 인지하기 위해서
        """
        return f"[{self.domain}] {self.name}"


class ActivityTag(models.Model):
    """ActivityAction과 Tag를 연결하는 릴레이션 테이블"""

    activity_action = models.ForeignKey(
        "activity_gallery.ActivityAction",  # 문자열로 참조
        on_delete=models.CASCADE,
        related_name="activity_tags",
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("activity_action", "tag")
        verbose_name = "활동 태그"
        verbose_name_plural = "활동 태그"

    def __str__(self):
        return f"{self.activity_action} - {self.tag}"


class NoticeTag(models.Model):
    notice_action = models.ForeignKey(
        "notice.Notice", on_delete=models.CASCADE, related_name="activity_tags"
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("notice_action", "tag")
        verbose_name = "공지 태그"
        verbose_name_plural = "공지 태그"

    def __str__(self):
        return f"{self.notice_action} - {self.tag}"
