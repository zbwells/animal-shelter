# Generated by Django 4.1.7 on 2023-03-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="estimated_age_months",
            field=models.IntegerField(default=0, verbose_name="Estimated Age (Months)"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="estimated_age",
            field=models.IntegerField(default=0, verbose_name="Estimated Age (Years)"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="id_num",
            field=models.IntegerField(unique=True, verbose_name="ID Number"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="notes",
            field=models.TextField(blank=True),
        ),
    ]