from django.db import models

from core.tag.models import TagModel

class ActivityTag(TagModel, models.Model):
    """활동 갤러리 태그 모델"""
    
    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "활동 태그 관리"

class ActivityTagRelation(models.Model):
    """커뮤니티 활동과 태그를 연결하는 중간 모델"""
    activity_action = models.ForeignKey(
        "ActivityAction", on_delete=models.CASCADE, related_name="activity_tags"
    )
    tag = models.ForeignKey(ActivityTag, on_delete=models.CASCADE, related_name="tag_relations")
    
    class Meta:
        unique_together = ("activity_action", "tag") # 중복 태그 방지

class ActivityAction(models.Model):
    """커뮤니티 활동 모델"""

    title = models.CharField(max_length=20, verbose_name="활동명")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="imgages/")
    content = models.TextField(verbose_name="내용")
    tags = models.ManyToManyField(ActivityTag, through="ActivityTagRelation", related_name="actions")

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
