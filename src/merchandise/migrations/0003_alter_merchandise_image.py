# Generated by Django 5.1.5 on 2025-03-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("merchandise", "0002_alter_merchandise_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="merchandise",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="썸네일 이미지"),
        ),
    ]
