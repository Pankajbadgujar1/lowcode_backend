from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    """
    Serializes form data to/from JSON.
    """
    class Meta:
        model = Form
        fields = ['id', 'name', 'description', 'schema', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
