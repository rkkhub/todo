from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from core.models import Task

from todo import serializers


class TaskViewSet(mixins.ListModelMixin,
                  #   mixins.CreateModelMixin,
                  #   mixins.UpdateModelMixin,
                  #   mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """ Class based view to Create, update, delete task"""
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
