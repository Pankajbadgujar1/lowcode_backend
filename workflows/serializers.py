from rest_framework import serializers
from .models import Workflow, Step, Transition

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Workflow
        fields = ['id', 'name', 'form', 'created_by', 'created_at', 'steps']
        read_only_fields = ['created_by', 'created_at']