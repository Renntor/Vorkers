from django.core.validators import MaxValueValidator
from django.db import models

from apps.workers.constants import (FULL_NAME_MAX_LENGTH,
                                    MAX_LENGTH_VALIDATOR_BRIGADE,
                                    SPECIALIZATION_MAX_LENGTH)


class Brigade(models.Model):
    """
    Модель бригады
    """

    number = models.PositiveSmallIntegerField(
        verbose_name='Номер бригады',
        help_text='Номер бригады',
        validators=[
            MaxValueValidator(
                MAX_LENGTH_VALIDATOR_BRIGADE,
                message='Значение не может быть больше,'
                        f'чем {MAX_LENGTH_VALIDATOR_BRIGADE}'
            )
        ]
    )

    class Meta:
        verbose_name = 'Номер бригады'
        verbose_name_plural = 'Номера бригады'

    def __str__(self):
        return f'Номер бригады {self.number}'


class Worker(models.Model):
    """
    Модель работника
    """

    full_name = models.CharField(
        max_length=FULL_NAME_MAX_LENGTH,
        verbose_name='ФИО',
        help_text='Фамилия, Имя, Отчество',
    )
    brigade_number = models.ManyToManyField(
        Brigade,
        verbose_name='Номера бригады',
        help_text='Номера бригады в которых работает работник',
    )
    salary = models.IntegerField(
        verbose_name='Зарплата',
        help_text='Зарплата работника',
    )
    specialization = models.CharField(
        max_length=SPECIALIZATION_MAX_LENGTH,
        verbose_name='Специализация',
        help_text='Специализация работника'
    )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f'{self.specialization} {self.full_name}'
