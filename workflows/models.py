from django.db import models
from django.conf import settings
from builder.models import Form

class Workflow(models.Model):
    """
    Represents a complete business workflow process.
    """
    name = models.CharField(max_length=255)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Step(models.Model):
    """
    Represents a single step within a workflow.
    """
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=255)
    assigned_role = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

class Transition(models.Model):
    """
    Defines the transition rules between steps.
    """
    from_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='from_transitions')
    to_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='to_transitions')
    condition = models.CharField(max_length=255, blank=True)  # Optional condition logic
