# Generated by Django 4.1.7 on 2023-03-05 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listing", "0003_alter_animal_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="image",
            field=models.FileField(default="", upload_to="uploads/%Y/%m/"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="estimated_dob",
            field=models.DateField(verbose_name="Estimated Date of Birth"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="intake_date",
            field=models.DateField(verbose_name="Intake Date"),
        ),
    ]