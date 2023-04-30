# Generated by Django 4.1.7 on 2023-04-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.FileField(
                blank=True, default="", null=True, upload_to="uploads/%Y/%m/"
            ),
        ),
    ]