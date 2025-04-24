from .views import LoginView, userProfileView, RegisterView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', userProfileView.as_view(), name= 'profile')

]

