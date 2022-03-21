from rest_framework import serializers

from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for task objects"""

    class Meta:
        model = Task
        fields = ('id', 'title', 'section', 'date', 'completed')
        read_only_fields = ('id',)
