# Generated by Django 5.1.4 on 2024-12-31 10:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brigade',
            name='number',
            field=models.PositiveSmallIntegerField(help_text='Номер бригады', validators=[django.core.validators.MaxValueValidator(32767, message='Значение не может быть больше,чем 32767')], verbose_name='Номер бригады'),
        ),
    ]
