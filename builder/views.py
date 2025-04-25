from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Form
from .serializers import FormSerializer

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_form(request):
    """
    Creates a new form with schema and metadata.
    """
    serializer = FormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_forms(request):
    """
    Lists all forms created by the current user.
    """
    forms = Form.objects.filter(created_by=request.user)
    serializer = FormSerializer(forms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_form(request, pk):
    """
    Retrieves a specific form by ID.
    """
    try:
        form = Form.objects.get(pk=pk, created_by=request.user)
    except Form.DoesNotExist:
        return Response({"error": "Form not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FormSerializer(form)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_form(request, pk):
    """
    Updates an existing form.
    """
    try:
        form = Form.objects.get(pk=pk, created_by=request.user)
    except Form.DoesNotExist:
        return Response({"error": "Form not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FormSerializer(form, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_form(request, pk):
    """
    Deletes a form by ID.
    """
    try:
        form = Form.objects.get(pk=pk, created_by=request.user)
    except Form.DoesNotExist:
        return Response({"error": "Form not found"}, status=status.HTTP_404_NOT_FOUND)

    form.delete()
    return Response({"message": "Form deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
