# Generated by Django 4.2.5 on 2024-03-10 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0003_apply"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apply",
            name="applydate",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="apply",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="job.job"
            ),
        ),
    ]
