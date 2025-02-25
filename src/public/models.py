from django.db import models


class Tag(models.Model):
    """
    참조 예시
    md는 임의의 models.py의 class라 가정

    class MdTag(models.Model):
        md = models.ForeignKey(Md, on_delete=models.CASCADE, related_name="md_tags")
        tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag_set")

        class Meta:
            unique_together = ('md', 'tag')
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
