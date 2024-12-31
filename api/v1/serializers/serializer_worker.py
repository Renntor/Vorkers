from rest_framework import serializers
from apps.workers.models import Worker, Brigade


class BrigadeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для номера бригады
    """

    class Meta:
        model = Brigade
        fields = ('number',)


class TeamSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с командой.
    """

    class Meta:
        model = Worker
        fields = ('id', 'full_name', 'specialization', 'salary')


class WorkerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работника.

    Поля:
    - number: Номер бригад работника
    """

    brigade_number = BrigadeSerializer(many=True, read_only=True)

    class Meta:
        model = Worker
        fields = ('id', 'full_name', 'salary',
                  'specialization', 'brigade_number')
