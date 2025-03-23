import os

from django.db import models

from public.models import ActivityTag, Tag


class ActivityAction(models.Model):
    """
    ### 커뮤니티 활동 모델
    """

    title = models.CharField(max_length=20, verbose_name="활동명")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="activity/thumbnail/")
    content = models.TextField(verbose_name="내용")
    tags = models.ManyToManyField(Tag, through=ActivityTag, related_name="actions")

    class Meta:
        verbose_name = "활동 갤러리"
        verbose_name_plural = "활동 갤러리"

    def delete(self, *args, **kwargs):
        # 썸네일 이미지 삭제
        if self.thumbnail and os.path.isfile(self.thumbnail.path):
            os.remove(self.thumbnail.path)

        # 연결된 모든 ActionPhoto 이미지 삭제
        for photo in self.photos.all():
            photo.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class ActionPhoto(models.Model):
    """커뮤니티 활동 사진 모델"""

    activity_action = models.ForeignKey(
        ActivityAction, on_delete=models.CASCADE, related_name="photos", null=True, blank=True
    )
    image = models.ImageField(upload_to="activity/action-photo/")

    def delete(self, *args, **kwargs):
        # 연결된 이미지 파일 삭제
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Photo for {self.activity_action.title if self.activity_action else 'No Activity'}"
