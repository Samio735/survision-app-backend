# Generated by Django 4.2.7 on 2023-11-08 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_survey_allresponses_survey_availableresponses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='surveys.survey'),
            preserve_default=False,
        ),
    ]
