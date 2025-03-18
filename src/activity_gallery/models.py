from django.db import models

from public.models import ActivityTag, Tag


class ActivityAction(models.Model):
    """
    ### 커뮤니티 활동 모델
    """

    title = models.CharField(max_length=20, verbose_name="활동명")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="imgages/")
    content = models.TextField(verbose_name="내용")
    tags = models.ManyToManyField(Tag, through=ActivityTag, related_name="actions")

    class Meta:
        verbose_name = "활동 갤러리"
        verbose_name_plural = "활동 갤러리"

    def __str__(self):
        return self.title


class ActionPhoto(models.Model):
    """커뮤니티 활동 사진 모델"""

    activity_action = models.ForeignKey(
        ActivityAction, on_delete=models.CASCADE, related_name="photos", null=True, blank=True
    )
    image = models.ImageField(upload_to="activity_photos/")

    def __str__(self):
        return f"Photo for {self.activity_action.title if self.activity_action else 'No Activity'}"
