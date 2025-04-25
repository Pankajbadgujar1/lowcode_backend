from django.urls import path
from .views import create_workflow, list_workflows, add_step, add_transition

urlpatterns = [
    path('create/', create_workflow, name='create_workflow'),
    path('list/', list_workflows, name='list_workflows'),
    path('step/add/', add_step, name='add_step'),
    path('transition/add/', add_transition, name='add_transition'),
]