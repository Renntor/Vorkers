from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from api.v1.serializers.serializer_worker import (TeamSerializer,
                                                  WorkerSerializer)
from apps.workers.models import Worker


class WorkersViewSet(ModelViewSet):
    """
    ViewSet для вывода данных о работнике
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TeamViewSet(ViewSet):
    """
    ViewSet для вывода всех работников указанной команды
    """

    @action(detail=True, methods=('GET',), url_path='WorkerList')
    def team(self, request, pk, *args, **kwargs):
        queryset = Worker.objects.filter(brigade_number__number=pk)
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
