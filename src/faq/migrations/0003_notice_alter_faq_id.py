# Generated by Django 5.1.5 on 2025-02-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0002_delete_notice_remove_faq_question_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="공지 제목")),
                ("content", models.TextField(verbose_name="공지 내용")),
            ],
            options={
                "verbose_name": "공지사항",
                "verbose_name_plural": "공지사항 목록",
            },
        ),
        migrations.AlterField(
            model_name="faq",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
