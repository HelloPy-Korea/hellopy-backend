# Generated by Django 5.1.5 on 2025-03-05 06:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notice", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notice",
            options={"verbose_name": "notice", "verbose_name_plural": "공지사항"},
        ),
    ]
