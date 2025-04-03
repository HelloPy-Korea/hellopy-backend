from django.db import models

from public.mixin.img_models import MultiImageFieldMixin
from public.tag_models import ActivityTag, Tag


class ActivityAction(MultiImageFieldMixin):
    """
    ### 커뮤니티 활동 모델
    """

    title = models.CharField(max_length=20, verbose_name="활동명")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="activity/thumbnail/")
    content = models.TextField(verbose_name="내용")
    tags = models.ManyToManyField(Tag, through=ActivityTag, related_name="actions")

    # MultiImageFieldMixin에서 clean, delete를 위해 필요한 정보 작성
    image_field_names = ["thumbnail"]

    class Meta:
        verbose_name = "활동 갤러리"
        verbose_name_plural = "활동 갤러리"

    def __str__(self):
        return self.title


class ActionPhoto(MultiImageFieldMixin):
    """커뮤니티 활동 사진 모델"""

    # 1:N 관계 표현을 위한 ForeignKey
    activity_action = models.ForeignKey(
        ActivityAction, on_delete=models.CASCADE, related_name="photos", null=True, blank=True
    )
    image = models.ImageField(upload_to="activity/action-photo/")

    # MultiImageFieldMixin에서 clean, delete를 위해 필요한 정보 작성
    image_field_names = ["image"]

    def __str__(self):
        return f"Photo for {self.activity_action.title if self.activity_action else 'No Activity'}"
