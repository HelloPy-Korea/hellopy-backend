# Generated by Django 5.1.5 on 2025-03-16 10:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("merchandise", "0003_alter_merchandise_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="merchandise",
            options={"verbose_name": "상품", "verbose_name_plural": "상품"},
        ),
    ]
