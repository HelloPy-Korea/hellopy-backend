# Generated by Django 5.1.5 on 2025-02-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0003_notice_alter_faq_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Notice",
        ),
        migrations.AlterField(
            model_name="faq",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
