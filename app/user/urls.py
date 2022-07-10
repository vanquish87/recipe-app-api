"""
URL mappings for the user API
"""
from django.urls import path
from user import views

# used in reverse function in test_user_api.py file
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
