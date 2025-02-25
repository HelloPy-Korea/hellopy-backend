from django.db import models

# Create your models here.


class Merchandise(models.Model):
    """
    ### MD 필드 정의
    """

    product_name = models.CharField(max_length=255)
    product_info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product_name
