#from .views import LoginView, userProfileView, RegisterView
from django.urls import path
from .views import  register_view, login_view, profile_view, logout_view

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('me/', userProfileView.as_view(), name= 'profile')

# ]

urlpatterns = [
    
    path('register/',register_view,name='register'),
    path('login/',login_view, name='login'),
    path('me/',profile_view, name='profile'),
    path('logout/',logout_view,name='logout')
]
