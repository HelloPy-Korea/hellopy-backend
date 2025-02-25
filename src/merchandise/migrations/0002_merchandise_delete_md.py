# Generated by Django 5.1.5 on 2025-02-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("merchandise", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Merchandise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=255)),
                ("product_info", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.DeleteModel(
            name="Md",
        ),
    ]
