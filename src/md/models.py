from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Md(models.Model):
    """
    ### MD 필드 정의
    """
    product_name = models.CharField(max_length=255)
    image_url = models.TextField()
    
    def __str__(self):
        return self.product_name
    
class MdTag(models.Model):
    md = models.ForeignKey(Md, on_delete=models.CASCADE, related_name="md_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag_set")
    
    class Meta:
        unique_together = ('md', 'tag')