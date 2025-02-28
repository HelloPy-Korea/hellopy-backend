from django.db import models

from public.models import Tag


class CommunityAction(models.Model):
    """커뮤니티 활동 모델"""

    title = models.CharField(max_length=20, verbose_name="활동명")
    content = models.TextField(verbose_name="내용")
    tags = models.ManyToManyField(Tag, through="CommunityTag", related_name="actions")

    def __str__(self):
        return self.title


class CommunityTag(models.Model):
    """커뮤니티 활동과 태그를 연결하는 모델"""

    community_action = models.ForeignKey(
        CommunityAction, on_delete=models.CASCADE, related_name="community_tags"
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("community_action", "tag")


class ActionPhoto(models.Model):
    """커뮤니티 활동 사진 모델"""

    community_action = models.ForeignKey(
        CommunityAction, on_delete=models.CASCADE, related_name="photos"
    )
    image = models.ImageField(upload_to="community_photos/")

    def __str__(self):
        return f"Photo for {self.community_action.title}"
