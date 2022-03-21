from rest_framework import viewsets, mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Task

from todo import serializers


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """ Class based view to Create, update, delete task"""
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        """Return object for the current use only"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Creates a new recipe with user assigned"""
        serializer.save(user=self.request.user)
