from django.urls import path
from .views import create_form, list_forms, get_form, update_form, delete_form

urlpatterns = [
    path('forms/', list_forms, name='list_forms'),
    path('forms/create/', create_form, name='create_form'),
    path('forms/<int:pk>/', get_form, name='get_form'),
    path('forms/<int:pk>/update/', update_form, name='update_form'),
    path('forms/<int:pk>/delete/', delete_form, name='delete_form'),
]
