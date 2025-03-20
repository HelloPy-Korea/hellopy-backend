# Generated by Django 5.1.5 on 2025-03-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public", "0005_tag_domain_alter_tag_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={
                "verbose_name": "전체 태그 관리",
                "verbose_name_plural": "전체 태그 관리",
            },
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, verbose_name="태그"),
        ),
    ]
