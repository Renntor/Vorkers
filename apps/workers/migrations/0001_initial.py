# Generated by Django 5.1.4 on 2024-12-30 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(help_text='Номер бригады', validators=[django.core.validators.MaxLengthValidator(32767, message='Значение не может быть больше,чем 32767')], verbose_name='Номер бригады')),
            ],
            options={
                'verbose_name': 'Номер бригады',
                'verbose_name_plural': 'Номера бригады',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Фамилия, Имя, Отчество', max_length=120, verbose_name='ФИО')),
                ('salary', models.IntegerField(help_text='Зарплата работника', verbose_name='Зарплата')),
                ('specialization', models.CharField(help_text='Специализация работника', max_length=120, verbose_name='Специализация')),
                ('brigade_number', models.ManyToManyField(help_text='Номера бригады в которых работает работник', to='workers.brigade', verbose_name='Номера бригады')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]